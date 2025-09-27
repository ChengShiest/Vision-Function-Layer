import json
import argparse

def calculate_accuracy(jsonl_file_path):
    """
    Calculates the accuracy from a JSONL file where each line contains
    'target' and 'filtered_resps'.

    Args:
        jsonl_file_path (str): The path to the JSONL file.

    Returns:
        float: The calculated accuracy, or 0.0 if no samples are found.
    """
    total_samples = 0
    correct_samples = 0

    try:
        with open(jsonl_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line.strip())
                    total_samples += 1

                    target = data.get('target')
                    filtered_resps = data.get('filtered_resps')

                    # Ensure both target and filtered_resps exist and filtered_resps is not empty
                    if target is not None and filtered_resps and isinstance(filtered_resps, list) and len(filtered_resps) > 0:
                        prediction = filtered_resps[0]
                        # Simple string comparison, adjust if more complex parsing is needed
                        if str(target) == str(prediction):
                            correct_samples += 1
                    else:
                        print(f"Warning: Skipping line due to missing 'target' or invalid 'filtered_resps': {line.strip()}")

                except json.JSONDecodeError:
                    print(f"Warning: Skipping invalid JSON line: {line.strip()}")
                except Exception as e:
                    print(f"Warning: Skipping line due to error: {e} - Line: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: File not found at {jsonl_file_path}")
        return 0.0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0.0

    if total_samples == 0:
        print("No samples found in the file.")
        return 0.0

    accuracy = correct_samples / total_samples
    print(f"Processed {total_samples} samples.")
    print(f"Correct predictions: {correct_samples}")
    print(f"Accuracy: {accuracy:.4f}")

    return accuracy

if __name__ == "__main__":
    # Example usage:
    # Create a dummy jsonl file for testing
    dummy_data = [
        {"doc_id": 0, "target": "B", "filtered_resps": ["B"]},
        {"doc_id": 1, "target": "C", "filtered_resps": ["A"]},
        {"doc_id": 2, "target": "A", "filtered_resps": ["A"]},
        {"doc_id": 3, "target": "D", "filtered_resps": ["D."]}, # Example of slight mismatch
        {"doc_id": 4, "target": "B", "filtered_resps": ["B"]},
        {"doc_id": 5, "target": "A", "filtered_resps": []}, # Example of empty response
        {"doc_id": 6, "target": "C"}, # Example of missing response
        {"doc_id": 7, "filtered_resps": ["C"]}, # Example of missing target
    ]
    dummy_file = "dummy_results.jsonl"
    with open(dummy_file, 'w', encoding='utf-8') as f:
        for item in dummy_data:
            f.write(json.dumps(item) + '\n')

    print(f"Calculating accuracy for dummy file: {dummy_file}")
    calculate_accuracy(dummy_file)

    print("\nCalculating accuracy using command-line arguments (if provided)")
    parser = argparse.ArgumentParser(description="Calculate accuracy from a JSONL results file.")
    parser.add_argument("file_path", help="Path to the JSONL file")
    args = parser.parse_args()

    calculate_accuracy(args.file_path)
