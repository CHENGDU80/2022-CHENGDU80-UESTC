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
    pos_sample_ids = [i for i in range(len(y_labels)) if y_labels[i] == 0]
    neg_sample_ids = [i for i in range(len(y_labels)) if y_labels[i] == 1]
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

def predict(posResDf, negResDf, resLabel, resScore, testDf):
    for index in range(len(testDf)):
        posRow = posResDf.loc[index]
        negRow = negResDf.loc[index]
        score = 0.2 * posRow.max() + 0.8 * (1 - negRow.max())
        score = posRow.max()
        if score <= thrs:
            resLabel.append(1)
        else:
            resLabel.append(0)
        resScore.append(score)

parser = argparse.ArgumentParser()
parser.add_argument('-thrs', type=float, default=0.5)

args = parser.parse_args()
thrs = args.thrs

answerFile = "feature.csv"
answerDate = "sample_submission.csv"
answerDf = pd.read_csv(answerFile)
usrID = answerDf["APPLICATION_ID"]
answerDate = pd.read_csv(answerDate)["APPLICATION_DATE"]

# testFilePath = "../data/test/constructed_testset.csv"
testFilePath = "constructed_testset.csv"
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
predict(posResDf, negResDf, resLabel, resScore, testDf)
# for index in range(len(testDf)):
#     posRow = posResDf.loc[index]
#     negRow = negResDf.loc[index]
#     score = 0.2 * posRow.max() + 0.8 * (1 - negRow.max())
#     score = posRow.max()
#     if score <= thrs:
#         resLabel.append(1)
#     else:
#         resLabel.append(0)
#     resScore.append(score)
# print(np.array(resScore).mean())
resLabel = np.array(resLabel)
labelDf = pd.DataFrame(resLabel, columns=["label"])
writeDf = pd.DataFrame(resScore, columns=["0"])
writeDf["1"] = writeDf.apply(lambda col: 1-col["0"], axis=1)
writeDf = pd.concat([usrID, answerDate, writeDf], axis=1)
# writeDf = pd.condat([],axis=1)
print(Counter(labelDf["label"]))
print(writeDf)
exit()
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