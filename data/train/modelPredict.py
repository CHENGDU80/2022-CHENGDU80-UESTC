import pandas as pd
import numpy as np
import os
import argparse
import joblib

from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

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
parser.add_argument('-thrs', type=float, default=0.5)
parser.add_argument("-testset", type=str, default="feature.csv")
parser.add_argument("-testlabel", type=str, default="../data/test/label.csv")
parser.add_argument('-num_models', type=int, default=20)

args = parser.parse_args()
thrs = args.thrs
testFile = args.testset
testLabel = args.testlabel
numModels = args.num_models
print("Threshold: " + str(thrs))
print("Test File: " + testFile)
print("Test Label: " + testLabel)
print("Model Nums: " + str(numModels))

submissionTestFile = "feature.csv"
submissionUsrInfo = "sample_submission.csv"
submissionFile = "UESTC_Submission.csv"
testFile = submissionTestFile

submissionTestDf = pd.read_csv(submissionTestFile)
submissionUsrInfo = pd.read_csv(submissionUsrInfo)
usrId = submissionUsrInfo["APPLICATION_ID"]
dateDf = submissionUsrInfo["APPLICATION_DATE"]

testDf = pd.read_csv(testFile)
testDf = testDf.drop("APPLICATION_ID", axis=1)
for column in testDf.columns:
    if testDf[column].isnull().sum() > len(testDf) * 0.5:
        testDf = testDf.drop(column, axis=1)
testDf = testDf.fillna(0)
originColumns = testDf.columns
testDf = pd.DataFrame(normalize(testDf), columns=originColumns)
print(testDf)
modelBase = "./models/Model_"
NUM_MODEL = numModels
modelRes_0 = []
modelRes_1 = []
modelFullRes = []
for i in tqdm(range(NUM_MODEL)):
    modelResultFile = modelBase + str(i) + ".m"
    svm_model = joblib.load(modelResultFile)
    resScore = svm_model.predict_proba(testDf)
    partialResScore_0 = resScore[:, 0]
    partialResScore_1 = resScore[:, 1]
    modelRes_0.append(partialResScore_0)
    modelRes_1.append(partialResScore_1)
    # modelRes.append(resScore)
# modelResArray = np.array(modelRes)
# print(modelResArray.shape)
modelScore_0 = np.mean(modelRes_0, axis=0)
print(modelScore_0.shape)
modelScore_1 = np.mean(modelRes_1, axis=0)
print(modelScore_1.shape)
modelResDf = pd.DataFrame({"0":modelScore_0, "1":modelScore_1})
print(modelResDf)
writeDf = pd.DataFrame()
writeDf = pd.concat([usrId, dateDf, modelResDf], ignore_index=True, axis=1)
writeDf.columns = ["APPLICATION_ID", "APPLICATION_DATE", "0", "1"]
print(writeDf)
writeDf.to_csv(submissionFile, sep=",", index=False)