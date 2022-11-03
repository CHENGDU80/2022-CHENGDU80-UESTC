'''
dataop.py：为模型组织数据输入
定义有函数：
    · ReadData：读取供训练的数据
    · ReadTestData：读取用于predict的数据
    · SplitDataSet：直接从总的数据集里分割出训练集和验证集
    · GetDataSet：读取已有的训练集和验证集
定义有类：
    · FeatureDataSet：继承自torch.utils.data.Dataset类，用于构造训练和验证的数据输入
'''
import torch
import pandas as pd
import numpy as np

from torch.utils.data import Dataset
from sklearn.preprocessing import StandardScaler
from torch.utils.data import SubsetRandomSampler
from collections import defaultdict

# TODO：读取数据供训练
def ReadData(dataPath):
    return None

# TODO：读取测试数据
def ReadTestData(testDataPath):
    return None

# 分割数据集为训练集和验证集
def SplitDataSet(dataPath, batchSize, val_p=0.2):
    modelDataSet = FeatureDataSet(dataPath)
    dataSetSize = len(modelDataSet)
    indices = list(range(dataSetSize))
    split = int(np.floor(val_p * dataSetSize))
    trainIndices, valIndices = indices[split:], indices[:split]
    # 初始化训练集和验证集的sampler
    trainSampler = SubsetRandomSampler(trainIndices)
    validSampler = SubsetRandomSampler(valIndices)
    # 构造dataLoader返回
    trainLoader = torch.utils.data.DataLoader(modelDataSet, batch_size=batchSize, sampler=trainSampler)
    validationLoader = torch.utils.data.DataLoader(modelDataSet, batch_size=batchSize, sampler=validSampler)
    return trainLoader, validationLoader

# 获取已保存的分好的数据集
def GetDataSet(trainDataPath, valDataPath, batchSize):
    traindata = FeatureDataSet(trainDataPath)
    valdata = FeatureDataSet(valDataPath)
    # 构造dataLoader返回
    trainLoader = torch.utils.data.DataLoader(traindata, batch_size=batchSize, shuffle=True)
    validationLoader = torch.utils.data.DataLoader(valdata, batch_size=batchSize, shuffle=True)
    return trainLoader, validationLoader

# 继承torch.utils.data.Dataset构造模型用Dataset
class FeatureDataSet(Dataset):
    def __init__(self, dataPath):
        self.data, self.label = ReadData(dataPath)

    def __getitem__(self, index):
        return self.data[index], self.label[index]

    def __len__(self):
        return len(self.data)