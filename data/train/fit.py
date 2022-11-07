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

parser = argparse.ArgumentParser()
parser.add_argument('-eps', type=float, default=0.08)
parser.add_argument('-min_samples', type=int, default=3)
parser.add_argument('-reTrain', type=bool, default=False)

args = parser.parse_args()
epsNum = args.eps
minSamples = args.min_samples
reTrainFlag = args.reTrain

trainFile = "../data/train/constructed_trainset.csv"
modelFile = "model.csv"
resultFile = "res"
originDf = pd.read_csv(trainFile)
data = np.array(originDf)

if reTrainFlag:
    db = DBSCAN(eps=epsNum, min_samples=minSamples, metric="cosine")
    ids = db.fit(data).labels_
    np.save(resultFile, ids)
else:
    ids = np.load(resultFile + ".npy")
idsCount = Counter(ids)
print(idsCount)
countCluster = ids.max()
print(countCluster)
clusterDf = pd.DataFrame(data = ids, columns=["ClusterID"])
originDf = pd.concat([originDf, clusterDf], axis=1)
print(originDf.head())
tmpDf = pd.DataFrame()
centerPointDf = pd.DataFrame()
for clusterIdx in range(countCluster+1):
    tmpDf = originDf[originDf["ClusterID"] == clusterIdx]
    centerPointDf = pd.concat([centerPointDf, tmpDf.mean().transpose()], axis = 1)

# print(centerPointDf.shape)
centerPointDf = centerPointDf.transpose()
centerPointDf.columns = originDf.columns
centerPointDf = centerPointDf.drop("ClusterID", axis=1)
# print(centerPointDf)
centerPointDf.to_csv(modelFile, index = True, sep=",")