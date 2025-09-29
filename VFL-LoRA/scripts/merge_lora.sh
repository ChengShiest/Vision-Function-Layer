#!/bin/bash

MODEL_NAME="Qwen/Qwen2.5-VL-7B-Instruct"
# MODEL_NAME="Qwen/Qwen2-VL-2B-Instruct"

export PYTHONPATH=src:$PYTHONPATH

python src/merge_lora_weights.py \
    --model-path /2022233235/Qwen2-VL-Finetune/output/0506-qwen2.5-vl-7b-lora-0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38-rank40\
    --model-base $MODEL_NAME  \
    --save-model-path /2022233235/Qwen2-VL-Finetune/output/0506-qwen2.5-vl-7b-lora-rank40 \
    --safe-serialization


# MODEL_NAME="Qwen/Qwen2.5-VL-7B-Instruct"
# # MODEL_NAME="Qwen/Qwen2-VL-2B-Instruct"

# export PYTHONPATH=src:$PYTHONPATH

# python src/merge_lora_weights.py \
#     --model-path /2022233235/Qwen2-VL-Finetune/output/0503-qwen2.5-vl-7b-lora-13,14,15,16,17,18,19,20,21,22,23 \
#     --model-base $MODEL_NAME  \
#     --save-model-path /2022233235/Qwen2-VL-Finetune/output/0503-qwen2.5-vl-7b-lora-13-23-merged \
#     --safe-serialization

