'''
validation.py：定义验证的流程
    · dataloader：数据，torch.utils.data.DataLoader型
    · model：模型
    · loss_fn：损失函数
    · device：计算设备
'''
import torch
from sklearn.metrics import confusion_matrix, f1_score, classification_report, precision_recall_fscore_support

def validation(dataloader, model, loss_fn, device):
    None