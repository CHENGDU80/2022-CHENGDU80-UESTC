import pandas as pd
import numpy as np
import math as mt
import os
import argparse
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

def SaveModel(model, outputFile, originData):
    idsCount = Counter(model)
    print(idsCount)
    countCluster = model.max()
    # print(countCluster)
    clusterDf = pd.DataFrame(data = model, columns=["ClusterID"])
    originData = pd.concat([originData, clusterDf], axis=1)
    # print(originData.head())
    tmpDf = pd.DataFrame()
    centerPointDf = pd.DataFrame()
    for clusterIdx in range(countCluster+1):
        tmpDf = originData[originData["ClusterID"] == clusterIdx]
        centerPointDf = pd.concat([centerPointDf, tmpDf.mean().transpose()], axis = 1)

    # print(centerPointDf.shape)
    centerPointDf = centerPointDf.transpose()
    centerPointDf.columns = originData.columns
    centerPointDf = centerPointDf.drop("ClusterID", axis=1)
    # print(centerPointDf)
    centerPointDf.to_csv(outputFile, index = True, sep=",")

parser = argparse.ArgumentParser()
parser.add_argument('-eps', type=float, default=0.08)
parser.add_argument('-min_samples', type=int, default=3)
parser.add_argument('-reTrain', type=bool, default=False)

args = parser.parse_args()
epsNum = args.eps
minSamples = args.min_samples
reTrainFlag = args.reTrain

posTrainFile = "../data/train/constructed_trainset.csv"
negTrainFile = "../data/train/constructed_trainset_neg.csv"
posModelFile = "posModel.csv"
negModelFile = "negModel.csv"
posResultFile = "posRes"
negResultFile = "negRes"
posDf = pd.read_csv(posTrainFile)
posData = np.array(posDf)

negDf = pd.read_csv(negTrainFile)
negData = np.array(negDf)

if reTrainFlag:
    db = DBSCAN(eps=epsNum, min_samples=minSamples, metric="cosine")
    posIds = db.fit(posData).labels_
    np.save(posResultFile, posIds)
    negIds = db.fit(negData).labels_
    np.save(negResultFile, negIds)
else:
    posIds = np.load(posResultFile + ".npy")
    negIds = np.load(negResultFile + ".npy")

SaveModel(posIds, posModelFile, posDf)
SaveModel(negIds, negModelFile, negDf)
exit()

idsCount = Counter(posIds)
print(idsCount)
countCluster = posIds.max()
print(countCluster)
clusterDf = pd.DataFrame(data = posIds, columns=["ClusterID"])
posDf = pd.concat([posDf, clusterDf], axis=1)
print(posDf.head())
tmpDf = pd.DataFrame()
centerPointDf = pd.DataFrame()
for clusterIdx in range(countCluster+1):
    tmpDf = posDf[posDf["ClusterID"] == clusterIdx]
    centerPointDf = pd.concat([centerPointDf, tmpDf.mean().transpose()], axis = 1)

# print(centerPointDf.shape)
centerPointDf = centerPointDf.transpose()
centerPointDf.columns = posDf.columns
centerPointDf = centerPointDf.drop("ClusterID", axis=1)
# print(centerPointDf)
centerPointDf.to_csv(posModelFile, index = True, sep=",")