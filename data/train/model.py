import pandas as pd
import numpy as np
import argparse
import os
import joblib

from collections import Counter
from sklearn.cluster import DBSCAN
from sklearn.svm import SVC
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from tqdm import tqdm

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
    auc = sum_indicator_value/(len(pos_sample_ids) * len(neg_sample_ids))
    return auc

def ModelForward(posModelDf, negModelDf, testDf):
    resScore = []
    posModelData = np.array(posModelDf)
    negModelData = np.array(negModelDf)
    testData = np.array(testDf)
    posCosData = cosine_similarity(testData, posModelData)
    negCosData = cosine_similarity(testData, negModelData)
    posResDf = pd.DataFrame(posCosData)
    negResDf = pd.DataFrame(negCosData)
    for index in range(len(testDf)):
        posRow = posResDf.loc[index]
        negRow = negResDf.loc[index]
        score = 0.2 * posRow.max() + 0.8 * (1 - negRow.max())
        resScore.append(score)
    return resScore

def SaveModel(model, outputFile, originData):
    idsCount = Counter(model)
    # print(idsCount)
    countCluster = model.max()
    # print(countCluster)
    clusterDf = pd.DataFrame(data = model, columns=["ClusterID"])
    # print(clusterDf)
    # print(originData.head())
    originData = originData.reset_index(drop=True)
    originData = pd.concat([originData, clusterDf], axis=1)
    # print(originData.head())
    tmpDf = pd.DataFrame()
    centerPointDf = pd.DataFrame()
    for clusterIdx in range(countCluster+1):
        # print(originData)
        tmpDf = originData[originData["ClusterID"] == clusterIdx]
        centerPointDf = pd.concat([centerPointDf, tmpDf.mean().transpose()], axis=1)

    # print(centerPointDf.shape)
    centerPointDf = centerPointDf.transpose()
    centerPointDf.columns = originData.columns
    centerPointDf = centerPointDf.drop("ClusterID", axis=1)
    # print(centerPointDf)
    centerPointDf.to_csv(outputFile, index = True, sep=",")
    return centerPointDf

def processFeature(originDf, labelDf):
    originDf = originDf.drop("APPLICATION_ID", axis=1)
    for column in originDf.columns:
        if originDf[column].isnull().sum() > len(originDf) * 0.5:
            originDf = originDf.drop(column, axis=1)
    originDf = originDf.fillna(0)
    originColumns = originDf.columns
    originDf = pd.DataFrame(normalize(originDf), columns=originColumns)
    
    posIndex = labelDf.loc[labelDf["DEFAULT_LABEL"] == 1].index
    negIndex = labelDf.loc[labelDf["DEFAULT_LABEL"] == 0].index
    posDf = originDf.drop(posIndex)
    posDf["Label"] = 0
    negDf = originDf.drop(negIndex)
    negDf["Label"] = 1
    return negDf, posDf, originDf

parser = argparse.ArgumentParser()
parser.add_argument('-eps', type=float, default=0.08)
parser.add_argument('-min_samples', type=int, default=3)
parser.add_argument('-reTrain', type=bool, default=True)
parser.add_argument('-thrs', type=float, default=0.5)
parser.add_argument('-num_models', type=int, default=50)
parser.add_argument('-train_set', type=str, default="../data/train/feature.csv")
parser.add_argument('-train_label', type=str, default="../data/train/label.csv")

args = parser.parse_args()
epsNum = args.eps
minSamples = args.min_samples
reTrainFlag = args.reTrain
thrs = args.thrs
numModels = args.num_models
trainSet = args.train_set
trainLabel = args.train_label

print("Threshold: " + str(thrs))
print("eps: " + str(epsNum))
print("Minimal Samples: " + str(minSamples))
print("reTrain Flag: " + reTrainFlag)
print("Model Nums: " + str(numModels))
print("Train Set: " + trainSet)
print("Train Label: " + trainLabel)

# trainSet = "../data/train/feature.csv"
# trainLabel = "../data/train/label.csv"
testFile = "../data/test/feature.csv"
testLabel = "../data/test/label.csv"
submissionTestFile = "feature.csv"
submissionUsrInfo = "sample_submission.csv"

submissionTestDf = pd.read_csv(submissionTestFile)
submissionUsrInfo = pd.read_csv(submissionUsrInfo)
usrId = submissionUsrInfo["APPLICATION_ID"]
dateDf = submissionUsrInfo["APPLICATION_DATE"]

featureDf = pd.read_csv(trainSet)
trainLabelDf = pd.read_csv(trainLabel)
testDf = pd.read_csv(testFile)
testLabelDf = pd.read_csv(testLabel)
negTrain, posTrain, featureDf = processFeature(featureDf, trainLabelDf)
negTest, posTest, testDf = processFeature(testDf, testLabelDf)

posModelBase = "./models/posModel_"
negModelBase = "./models/negModel_"
modelBase = "./models/Model_tmp_"

NUM_MODEL = numModels
modelRes = []
modelFullRes = []
if not os.path.exists("./models"):
    os.mkdir("./models")
for i in tqdm(range(NUM_MODEL)):
    modelPosData = posTrain.sample(frac=(1 / NUM_MODEL))
    modelNegData = negTrain.sample(frac=1, replace=True)
    modelData = pd.concat([modelPosData, modelNegData], axis = 0, ignore_index=True, join="inner")
    labels = modelData["Label"]
    modelData = modelData.drop("Label", axis=1)
    # exit()
    posResultFile = posModelBase + str(i) + ".m"
    negResultFile = negModelBase + str(i) + ".m"
    modelResultFile = modelBase + str(i) + ".m"
    if reTrainFlag:
        # print(testDf.head(5))
        # exit()
        svm_trainer = SVC(C=1, kernel='rbf', gamma='auto', coef0=0.0, tol=1e-3, probability = True)
        svm_trainer.fit(modelData, labels)
        joblib.dump(svm_trainer, modelResultFile)
        
        # resLabel = svm_trainer.predict(testDf)
        resScore = svm_trainer.predict_proba(testDf)
        partialResScore = resScore[:, 0]
        modelRes.append(partialResScore)
        modelFullRes.append(resScore)
    else:
        svm_trainer = joblib.load(modelResultFile)
        resScore = svm_trainer.predict_proba(testDf)
        partialResScore = resScore[:, 0]
        modelRes.append(partialResScore)
        modelFullRes.append(resScore)
        # print(resScore.shape)
        # print(resScore)
        # exit()
    #     db = DBSCAN(eps=epsNum, min_samples=minSamples, metric="cosine")
    #     posIds = db.fit(modelPosData).labels_
    #     negIds = db.fit(modelNegData).labels_
    #     posModelDf = SaveModel(posIds, posResultFile, modelPosData)
    #     negModelDf = SaveModel(negIds, negResultFile, modelNegData)
    # else:
    #     posModelDf = pd.read_csv(posResultFile).drop("Unnamed: 0", axis=1)
    #     negModelDf = pd.read_csv(negResultFile).drop("Unnamed: 0", axis=1)
    # modelRes.append(ModelForward(posModelDf, negModelDf, testDf))

# modelFullRes = np.array(modelFullRes)
# resScoreDf = pd.DataFrame(modelFullRes.transpose(), columns=["0", "1"])
# print(resScoreDf.head(5))
modelLabel = []
modelResArray = np.array(modelRes)
print(modelResArray.shape)
# exit()
modelScore = np.mean(np.abs(modelResArray), axis=0)
print(np.mean(modelScore))
countNeg = 0
for score in modelScore:
    if score <= thrs:
        modelLabel.append(1)
        countNeg += 1
    else:
        modelLabel.append(0)
print(countNeg)
testLabelDf = testLabelDf["DEFAULT_LABEL"]
convertActualLabel = testLabelDf.apply(lambda x:1 if x == 0  else 0)

acc = accuracy_score(modelLabel, testLabelDf)
print("Accuracy: " + str(acc))
precisioin = precision_score(modelLabel, convertActualLabel)
print("Precision: " + str(precisioin))
recall = recall_score(modelLabel, convertActualLabel)
print("Recall: " + str(recall))
f1score = f1_score(modelLabel, convertActualLabel)
print("F1: " + str(f1score))
AUC = calAUC(testLabelDf, modelScore)
print("AUC: " + str(AUC))