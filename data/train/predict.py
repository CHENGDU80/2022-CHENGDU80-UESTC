import pandas as pd
import numpy as np
import os
import argparse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score
from collections import Counter

def calAUC(y_labels, y_scores):
    pos_sample_ids = [i for i in range(len(y_labels)) if y_labels[i] == 0]
    neg_sample_ids = [i for i in range(len(y_labels)) if y_labels[i] == 1]
    sum_indicator_value = 0
    for i in pos_sample_ids:
        for j in neg_sample_ids:
            if y_scores[i] > y_scores[j]:
                sum_indicator_value += 1
            elif y_scores[i] <= y_scores[j]:
                sum_indicator_value += 0.5
    auc = sum_indicator_value/(len(pos_sample_ids) * len(neg_sample_ids))
    return auc

parser = argparse.ArgumentParser()
parser.add_argument('-thrs', type=float, default=0.5)

args = parser.parse_args()
thrs = args.thrs

testFilePath = "../data/test/constructed_testset.csv"
testLabelFilePath = "../data/test/label.csv"
modelPath = "model.csv"
testDf = pd.read_csv(testFilePath)
testData = np.array(testDf)
modelDf = pd.read_csv(modelPath).drop("Unnamed: 0", axis=1)
modelData = np.array(modelDf)
cosData = cosine_similarity(testData, modelData)
res = np.max(cosData, axis=1)
resDf = pd.DataFrame(cosData)
resLabel = []
resScore = []
count = 0
for index, row in resDf.iterrows():
    if row.max() <= thrs:
        count += 1
        resLabel.append(0)
        resScore.append(row.max())
    else:
        resLabel.append(1)
        resScore.append(row.max())
print(count)
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