#!/usr/bin/env python3
import torch
from mmaction.apis import init_recognizer, inference_recognizer

config_file = '../configs/recognition/tsn/tsn_r50_video_inference_1x1x3_100e_kinetics400_rgb.py'
#device = 'cuda:0' # 或 'cpu'
device = 'cpu:0' # 或 'cpu'
device = torch.device(device)

model = init_recognizer(config_file, device=device)
# 进行演示视频的推理
inference_recognizer(model, '../demo/demo.mp4')
