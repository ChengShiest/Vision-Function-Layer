


python3 -m accelerate.commands.launch \
    --main_process_port 10087 \
    --num_processes=8 \
    -m lmms_eval \
    --model qwen2_5_vl \
    --model_args pretrained="Qwen/Qwen2.5-VL-3B-Instruct,use_flash_attention_2=True" \
    --tasks  mme,chartqa\
    --batch_size 1 \
    --drop 4 \
    --log_samples \
    --log_samples_suffix pro-$NAME \
    --output_path ./logs/drop4-$NAME

python3 -m accelerate.commands.launch \
    --main_process_port 10087 \
    --num_processes=8 \
    -m lmms_eval \
    --model qwen2_5_vl \
    --model_args pretrained="Qwen/Qwen2.5-VL-3B-Instruct,use_flash_attention_2=True" \
    --tasks  mme,chartqa\
    --batch_size 1 \
    --drop 8 \
    --log_samples \
    --log_samples_suffix pro-$NAME \
    --output_path ./logs/drop8-$NAME

# python3 -m accelerate.commands.launch \
#     --main_process_port 10087 \
#     --num_processes=8 \
#     -m lmms_eval \
#     --model qwen2_5_vl \
#     --model_args pretrained="Qwen/Qwen2.5-VL-3B-Instruct,use_flash_attention_2=True" \
#     --tasks  mme,chartqa\
#     --batch_size 1 \
#     --drop 16 \
#     --log_samples \
#     --log_samples_suffix pro-$NAME \
#     --output_path ./logs/drop16-$NAME

# python3 -m accelerate.commands.launch \
#     --main_process_port 10087 \
#     --num_processes=8 \
#     -m lmms_eval \
#     --model qwen2_5_vl \
#     --model_args pretrained="Qwen/Qwen2.5-VL-3B-Instruct,use_flash_attention_2=True" \
#     --tasks  mme,chartqa\
#     --batch_size 1 \
#     --drop 20 \
#     --log_samples \
#     --log_samples_suffix pro-$NAME \
#     --output_path ./logs/drop20-$NAME
    