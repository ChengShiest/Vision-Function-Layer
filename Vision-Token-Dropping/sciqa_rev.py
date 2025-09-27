import json
import argparse
import re
import os

def extract_option_simple(text):
    """
    Extracts the first uppercase letter (option choice) from the beginning of a string.
    Handles cases like "A.", "(B)", " C ", etc.
    """
    if not isinstance(text, str):
        return None
    # Remove leading/trailing whitespace
    cleaned_text = text.strip()
    # Match variations like "A", "A.", "(A)"
    match = re.match(r"^\(?([A-Z])\)?\.?", cleaned_text)
    if match:
        return match.group(1)
    return None # Return None if no valid option format is found at the beginning

def calculate_accuracy(filepath):
    """
    Calculates the accuracy by comparing 'target' and 'filtered_resps'/'resps'
    from a JSONL file.
    """
    total = 0
    correct = 0
    skipped_missing_target = 0
    skipped_missing_response = 0
    skipped_json_error = 0
    skipped_processing_error = 0

    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return 0.0

    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            lineno = i + 1
            try:
                data = json.loads(line)
                doc_id = data.get('doc_id', f'line_{lineno}') # Use doc_id or line number for logging

                target = data.get("target")
                # Use filtered_resps if available, otherwise fall back to resps
                responses = data.get("filtered_resps", data.get("resps"))

                # --- Validation ---
                if target is None:
                    # print(f"Warning: Missing 'target' in line {lineno} (ID: {doc_id}). Skipping.")
                    skipped_missing_target += 1
                    continue # Skip lines without a target

                if responses is None or not isinstance(responses, list) or not responses:
                    # print(f"Warning: Missing or invalid 'filtered_resps'/'resps' in line {lineno} (ID: {doc_id}). Counting as incorrect.")
                    skipped_missing_response += 1
                    total += 1 # Count towards total, but it will be marked incorrect
                    continue

                # --- Extract Prediction ---
                # Take the first response from the list
                prediction_raw = responses[0]
                # Handle potential nested lists like [["A."]]
                if isinstance(prediction_raw, list):
                    if not prediction_raw:
                         # print(f"Warning: Empty inner list in response for line {lineno} (ID: {doc_id}). Counting as incorrect.")
                         skipped_missing_response += 1
                         total += 1
                         continue
                    prediction_raw = prediction_raw[0] # Take first element of inner list

                if not isinstance(prediction_raw, str):
                     # print(f"Warning: Prediction is not a string in line {lineno} (ID: {doc_id}). Prediction: {prediction_raw}. Counting as incorrect.")
                     skipped_missing_response += 1
                     total += 1
                     continue

                # --- Extract Options ---
                target_option = extract_option_simple(target)
                prediction_option = extract_option_simple(prediction_raw)

                # --- Comparison ---
                total += 1 # Increment total count for valid, processable lines

                if target_option is None:
                    print(f"Warning: Could not extract valid option from target '{target}' in line {lineno} (ID: {doc_id}). Counting as incorrect.")
                    # Still counts towards total, but marked incorrect
                elif prediction_option is None:
                    # print(f"Warning: Could not extract valid option from prediction '{prediction_raw}' in line {lineno} (ID: {doc_id}). Counting as incorrect.")
                    # Still counts towards total, but marked incorrect
                    pass # Prediction is None, so it won't match target_option
                elif prediction_option == target_option:
                    correct += 1
                # else: # Optional: Log mismatches for debugging
                    # print(f"Mismatch line {lineno} (ID: {doc_id}): Target='{target}' ({target_option}), Pred='{prediction_raw}' ({prediction_option})")


            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line {lineno}: {line.strip()}")
                skipped_json_error += 1
            except Exception as e:
                print(f"Error processing line {lineno} (ID: {doc_id if 'doc_id' in locals() else 'unknown'}): {line.strip()} - {e}")
                skipped_processing_error += 1

    # --- Results ---
    print("\n--- Calculation Summary ---")
    if total == 0:
        print("No processable lines found with both target and response.")
        accuracy = 0.0
    else:
        accuracy = correct / total
        print(f"Total lines processed (with target & response): {total}")
        print(f"Correct predictions: {correct}")
        print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")

    # Optional: Print skipped line counts
    if skipped_missing_target > 0:
        print(f"Lines skipped (missing target): {skipped_missing_target}")
    if skipped_missing_response > 0:
        print(f"Lines counted as incorrect (missing/invalid response): {skipped_missing_response}")
    if skipped_json_error > 0:
        print(f"Lines skipped (JSON decode error): {skipped_json_error}")
    if skipped_processing_error > 0:
        print(f"Lines skipped (other processing error): {skipped_processing_error}")

    return accuracy

if __name__ == "__main__":
    # Set up argument parser to get the file path from command line
    parser = argparse.ArgumentParser(
        description="Calculate accuracy from a JSONL prediction file (e.g., ScienceQA format). "
                    "Compares the first letter of 'target' and the first response in 'filtered_resps' or 'resps'."
    )
    parser.add_argument("filepath", help="Path to the JSONL file containing predictions.")
    # Example usage: python sciqa_rev.py path/to/your_predictions.jsonl
    args = parser.parse_args()

    calculate_accuracy(args.filepath)
