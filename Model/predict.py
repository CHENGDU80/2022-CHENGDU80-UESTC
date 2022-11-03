'''
predict.py：预测入口，完成流程：
    · 参数解析
    · 模型读取
    · 测试数据读取
    · 测试结果保存
'''
from model import TmpModel

import torch
from torch.nn.functional import softmax
import argparse
import json
import os
from collections import defaultdict

# XXX：参考往年预测，返回Top1和所有预测输出
def predict(testData, model, device):
    model.eval()
    with torch.no_grad():
        testData = torch.from_numpy(testData).to(device).to(torch.float32)
        pred = softmax(model(testData), dim=1)

    return pred.argmax(1), pred

if __name__ == '__main__':
    # TODO：参数解析
    parser = argparse.ArgumentParser()
    # 数据相关参数
    parser.add_argument('-model_path', type=str, default="./SavedModel/myModel.pth")
    parser.add_argument('-test_data', type=str, default="./data/testing_data/Constructed-28/final_constructed1.csv")
    parser.add_argument('-save_dir', type=str, default="./data/testing_data/Constructed-28/")
    # 计算设备
    parser.add_argument('-device', type=str, default='cuda')
    # 模型相关参数
    parser.add_argument('-dropout_p', type=float, default=0.2)
    parser.add_argument('-batch_size', type=int, default=32)

    args = parser.parse_args()
    # TODO：预测结果存储路径
    save_path_pred = args.save_dir + 'pred_' + os.path.basename(args.test_data)
    save_path_pvec = args.save_dir + 'pvec_' + os.path.basename(args.test_data)
    save_path_fres = args.save_dir + 'fres2_' + os.path.basename(args.test_data)[:-4] + '.txt'
    # 获取计算设备，默认GPU
    args.device = args.device if torch.cuda.is_available() else "cpu"
    print("Using {} device".format(args.device))
    # TODO：初始化模型
    predictModel = TmpModel(device=args.device).to(args.device)
    # 加载模型
    predictModel.load_state_dict(torch.load(args.model_path, map_location=args.device))

    # TODO：获取测试数据
    testData = None
    # 测试
    res, pvec = predict(testData, predictModel, device=args.device)
    # TODO：存储测试结果