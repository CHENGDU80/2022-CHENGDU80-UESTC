import pandas as pd
import numpy as np
import os
import argparse
import random
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score
from collections import Counter

def calAUC(y_labels, y_scores):
    pos_sample_ids = [i for i in range(len(y_labels)) if y_labels[i] == 1]
    neg_sample_ids = [i for i in range(len(y_labels)) if y_labels[i] == 0]
    sum_indicator_value = 0
    fault = 0
    for i in pos_sample_ids:
        for j in neg_sample_ids:
            if y_scores[i] > y_scores[j]:
                sum_indicator_value += 1
                fault += 1
            elif y_scores[i] == y_scores[j]:
                sum_indicator_value += 0.5
        # print(fault)
        # break
    auc = sum_indicator_value/(len(pos_sample_ids) * len(neg_sample_ids))
    return auc

parser = argparse.ArgumentParser()
parser.add_argument('-thrs', type=float, default=0.5)

args = parser.parse_args()
thrs = args.thrs

testFilePath = "../data/test/constructed_testset.csv"
testLabelFilePath = "../data/test/label.csv"
posModelPath = "posModel.csv"
negModelPath = "negModel.csv"
testDf = pd.read_csv(testFilePath)
testData = np.array(testDf)
posModelDf = pd.read_csv(posModelPath).drop("Unnamed: 0", axis=1)
posModelData = np.array(posModelDf)
negModelDf = pd.read_csv(negModelPath).drop("Unnamed: 0", axis=1)
negModelData = np.array(negModelDf)
posCosData = cosine_similarity(testData, posModelData)
negCosData = cosine_similarity(testData, negModelData)
res = np.max(posCosData, axis=1)
posResDf = pd.DataFrame(posCosData)
negResDf = pd.DataFrame(negCosData)
# print(posResDf.shape)
# print(negResDf.shape)
# print(posResDf.loc[0])
# print(negResDf.loc[0])
# print(len(testDf))
# exit()
resLabel = []
resScore = []
count = 0
for index in range(len(testDf)):
    posRow = posResDf.loc[index]
    negRow = negResDf.loc[index]
    score = (posRow.max() + (1 - negRow.max())) / 2
    score = posRow.max()
    if score <= thrs:
        count += 1
        resLabel.append(1)
        resScore.append(score)
    else:
        resLabel.append(0)
        resScore.append(score)
print(count)
# print(np.array(resScore).mean())
resLabel = np.array(resLabel)
actualLabel = pd.read_csv(testLabelFilePath)["DEFAULT_LABEL"]
print(Counter(actualLabel.values))
# 直接调库会有问题，0为正例1为反例
convertActualLabel = actualLabel.apply(lambda x:1 if x == 0  else 0)
print(Counter(actualLabel.values))

acc = accuracy_score(resLabel, convertActualLabel)
print("Accuracy: " + str(acc))
precisioin = precision_score(resLabel, convertActualLabel)
print("Precision: " + str(precisioin))
recall = recall_score(resLabel, convertActualLabel)
print("Recall: " + str(recall))
f1score = f1_score(resLabel, convertActualLabel)
print("F1: " + str(f1score))
AUC = calAUC(actualLabel, resScore)
print("AUC: " + str(AUC))