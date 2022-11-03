'''
model.py:完成模型定义
    __init__：类的初始化，定义基本模型结构
    forward()：一个batch的前向传播流程定义
'''

import torch
from torch import nn
import torch.nn.functional as F
import math

class TmpModel(nn.Module):
    # TODO：模型参数待定义，目前仅供参考
    def __init__(self, device='cuda', dropout_p=0.1, model_num=5, input_size=17, hidden_size=64, 
                 output_size=5, submodel_output_size=16, batch_size=32):
        super(TmpModel, self).__init__()
        
        self.device = device
        self.dropout = nn.Dropout(dropout_p)
        self.model_num = model_num
        self.input_size = input_size
        self.output_size = output_size
        self.submodel_output_size = submodel_output_size
        self.hidden_size = hidden_size
        self.batch_size = batch_size

        # XXX参考：往届MLP序列定义
        self.subModels = nn.ModuleList([
            nn.Sequential(
                nn.Linear(self.input_size, self.hidden_size),
                nn.Dropout(dropout_p),
                nn.ReLU(),
                nn.Linear(self.hidden_size, self.submodel_output_size)) 
                for i in range(self.model_num)])
        # XXX参考：往届输出全连接层定义
        self.outputLayer = nn.Sequential(
            nn.Linear(self.submodel_output_size * self.model_num, self.hidden_size),
            nn.Dropout(dropout_p),
            nn.ReLU(),
            nn.Linear(self.hidden_size, self.output_size),
        )
    
    # TODO：模型前向传播流程待定义
    def forward(self, batchData):
        # TODO：定义训练的参数
        self.weight = nn.parameter(torch.rand((batchData.shape[0], self.submodel_output_size, self.model_num)),
                                         requires_grad=True).to(self.device)
        return batchData