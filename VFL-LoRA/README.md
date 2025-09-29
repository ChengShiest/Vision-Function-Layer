# Vision-Function-Layer in Multimodal LLMs

This repository contains the implementation of **VFL-LoRA**, a method that leverages Vision-Function-Layers (VFL) to achieve efficient finetuning in Multimodal Large Language Models (MLLMs).

---

## Installation

Clone the repository and install dependencies:

```bash
conda env create -f environment.yaml
conda activate train
pip install qwen-vl-utils
pip install flash-attn --no-build-isolation

or

pip install -r requirements.txt -f https://download.pytorch.org/whl/cu128
pip install qwen-vl-utils
pip install flash-attn --no-build-isolation
```
## Usage

After installation, you can reproduce the results by running:

```bash
bash scripts/finetune_lora_vision.sh {layer_index}
```

## Acknowledgement

This codebase is built upon [Qwen2-VL-Finetune](https://github.com/2U1/Qwen2-VL-Finetune).  
We sincerely thank the authors for their excellent work.
