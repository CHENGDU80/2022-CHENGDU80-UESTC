'''
fit.py：模型训练入口，完成包括：
    · 参数解析
    · 模型对象初始化
    · 训练数据读取
    · 模型训练
    · 模型保存
'''
from model import TmpModel
from train import train
from validation import validation

import argparse
import torch
from torch import nn
import os

if __name__ == '__main__':
    # 参数解析
    parser = argparse.ArgumentParser()
    # TODO：数据操作相关参数
    parser.add_argument('-data_type', type=bool, default=False)
    # TODO：模型超参数
    parser.add_argument('-batch_size', type=int, default=256)
    parser.add_argument('-epoch', type=int, default=20)
    parser.add_argument('-lr', type=float, default=0.01)
    # 训练设备，默认GPU环境，本地调试用CPU
    parser.add_argument('-device', type=str, default='cuda')
    # 模型存储目录位置
    parser.add_argument('-model_save_dir', type=str, default='./SavedModel/')

    args = parser.parse_args()
    model_save_file = args.model_save_dir + "myModel.pth"

    # Get cpu or gpu device for training.
    args.device = args.device if torch.cuda.is_available() else "cpu"
    print("Using {} device".format(args.device))

    # TODO：模型对象初始化
    ourModel = TmpModel(device=args.device).to(args.device)

    # loss函数和优化器选择
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(ourModel.parameters(), lr=args.lr)

    # TODO：获取训练集和验证集
    train_dataloader = None
    val_dataloader = None
    # print('Training Data Size: ', len(train_dataloader) * args.batch_size)
    # print('Validation Data Size: ', len(val_dataloader) * args.batch_size)

    for t in range(args.epoch):
        print(f"Epoch {t + 1}\n-------------------------------")
        # 一个Epoch训练流程调train()
        train(dataloader=train_dataloader, model=ourModel, loss_fn=loss_fn, optimizer=optimizer, device=args.device)
        # 训练完后调validation()查看训练中途输出
        validation(dataloader=val_dataloader, model=ourModel, loss_fn=loss_fn, device=args.device)
    
    if not os.path.exists(model_save_file):
        os.mkdir(args.model_save_dir)
    torch.save(ourModel.state_dict(), model_save_file)
    print("Saved PyTorch Model State to model.pth: {}".format(model_save_file))
    print("Training Done!")
