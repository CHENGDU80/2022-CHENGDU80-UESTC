import pandas as pd
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score


testFilePath = "../data/test/constructed_testset.csv"
testLabelFilePath = "../data/test/label.csv"
modelPath = "model.csv"
testDf = pd.read_csv(testFilePath)
testData = np.array(testDf)
modelDf = pd.read_csv(modelPath).drop("Unnamed: 0", axis=1)
modelData = np.array(modelDf)
cosData = cosine_similarity(testData, modelData)
print(cosData)
print(cosData.shape)
res = np.max(cosData, axis=1)
print(res)
print(res.shape)
resDf = pd.DataFrame(cosData)
resLabel = []
print(resDf)
count = 0
for index, row in resDf.iterrows():
    if row.max() < 0.55:
        count += 1
        resLabel.append(1)
        # resDf["label"] = 1
    else:
        # resDf["label"] = 0
        resLabel.append(0)
print(count)
resLabel = np.array(resLabel)
print(resLabel)
# resLabel = resDf["label"]
# exit()
actualLabel = pd.read_csv(testLabelFilePath)["DEFAULT_LABEL"]

acc = accuracy_score(resLabel, actualLabel)
print("Accuracy: " + str(acc))
precisioin = precision_score(resLabel, actualLabel)
print("Precision: " + str(precisioin))
recall = recall_score(resLabel, actualLabel)
print("Recall: " + str(recall))
f1score = f1_score(resLabel, actualLabel)
print("F1: " + str(f1score))
AUC = roc_auc_score(actualLabel, resLabel)
print("AUC: " + str(AUC))