import pandas as pd
import numpy as np
import math as mt
import os
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
trainFile = r"../data/train/feature.csv"
labelFile = r"../data/train/label.csv"
clusterFile = r"../data/cluster_out.csv"

originDf = pd.read_csv(trainFile)
labelDf = pd.read_csv(labelFile)

for column in originDf.columns:
    if originDf[column].isnull().sum() > len(originDf) * 0.9:
        originDf = originDf.drop(column, axis=1)
print(originDf.shape)
originDf = originDf.fillna(0)
index = labelDf.loc[labelDf["DEFAULT_LABEL"] == 1].index
originDf = originDf.drop(index)
print(originDf.shape)
if "APPLICATION_ID" in originDf.columns:
    originDf = originDf.drop("APPLICATION_ID", axis=1)
#new_data=np.load('cos_data.npy')

new_data=np.transpose(originDf)

if not os.path.exists("cos_data.npy"):
    cos_data = cosine_similarity(new_data, new_data)
    np.save(r"cos_data",cos_data)
else:
    cos_data = np.load(r"cos_data.npy")
# exit()
#
# db = DBSCAN(eps=0.08, min_samples=5,metric='cosine')
# ids = db.fit(data).labels_
kmeans = KMeans(n_clusters=20, random_state=0).fit(cos_data)
ids = kmeans.labels_
print(ids)
print(len(ids))
features = pd.DataFrame(data = originDf.columns, columns=["Feature"])
clusterId = pd.DataFrame(data = ids, columns=["ClusterID"])
writeDf = pd.DataFrame()
writeDf = pd.concat([features, clusterId], axis=1)
writeDf.to_csv(clusterFile, index=False, sep=",")
print(writeDf)
