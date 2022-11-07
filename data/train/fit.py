import pandas as pd
import numpy as np
import math as mt
import os
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

trainFile = "../data/train/constructed_trainset.csv"
modelFile = "model.csv"
resultFile = "res"
originDf = pd.read_csv(trainFile)
data = np.array(originDf)

if not os.path.exists(resultFile + ".npy"):
    db = DBSCAN(eps=0.08, min_samples=3, metric="cosine")
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
    # print(tmpDf.mean())
# tmpDf = originDf[originDf["ClusterID"] == -1]
# print(tmpDf)
# centerPointDf = pd.concat([centerPointDf, tmpDf.transpose()], axis = 1)
print(centerPointDf.shape)
centerPointDf = centerPointDf.transpose()
centerPointDf.columns = originDf.columns
centerPointDf = centerPointDf.drop("ClusterID", axis=1)
# print(centerPointDf)
centerPointDf.to_csv(modelFile, index = True, sep=",")
# for usrIndex in len(ids):
#     clusterId = ids[usrIndex]