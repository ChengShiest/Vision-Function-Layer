We utilize the excellent open-source project [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) for evaluation. We sincerely thank the authors for providing such a valuable tool to the community.



## Installation

Clone the repository and install dependencies in editable mode:

```bash
pip install -e .
```

:warning: The `huggingface` package version should be exactly as `4.50.0` or you should modify the vision token swapping code based on your own version.

## Usage
After installation, you can reproduce Table 1 results by running:
```bash
bash run.sh
```