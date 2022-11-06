import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from tqdm import tqdm

originTrainPath = "./train/feature.csv"
originTestPath = "./test/feature.csv"
clusterPath = "./cluster_out.csv"
constructedTrainPath = "./train/constructed_trainset.csv"
constructedTestPath = "./test/constructed_testset.csv"
originTrainDf = pd.read_csv(originTrainPath)
originTestDf = pd.read_csv(originTrainPath)
clusterDf = pd.read_csv(clusterPath)
constructTrainDf = pd.DataFrame()
constructTestDf = pd.DataFrame()

originTrainDf = originTrainDf.fillna(0)
originTrainDf = originTrainDf.drop("APPLICATION_ID", axis=1)
originTestDf = originTestDf.fillna(0)
originTestDf = originTestDf.drop("APPLICATION_ID", axis=1)
# print(originDf.head(5))
# print(clusterDf.head(5))
# print(constructDf)
pca = PCA(n_components=1)
for clusterID in tqdm(range(20)):
    tmpTrainDf = pd.DataFrame()
    tmpTestDf = pd.DataFrame()
    for _, row in clusterDf.iterrows():
        if row["Cluster"] == clusterID:
            # print(originDf[row["Feature"]])
            tmpTrainDf = pd.concat([tmpTrainDf, originTrainDf[row["Feature"]]], sort=False, axis=1)
            tmpTestDf = pd.concat([tmpTestDf, originTestDf[row["Feature"]]], sort=False, axis=1)
    tmpTrainData = np.array(tmpTrainDf)
    tmpTrainData = normalize(tmpTrainData)
    tmpTestData = np.array(tmpTestDf)
    tmpTestData = normalize(tmpTestData)
    constructedTrainData = pca.fit_transform(tmpTrainData)
    constructedTestData = pca.fit_transform(tmpTestData)
    # print(constructedData)
    tmpTrainDf = pd.DataFrame(constructedTrainData, columns=["f{0}".format(clusterID)])
    tmpTestDf = pd.DataFrame(constructedTestData, columns=["f{0}".format(clusterID)])
    constructTrainDf = pd.concat([constructTrainDf, tmpTrainDf], sort=False, axis=1)
    constructTestDf = pd.concat([constructTestDf, tmpTestDf], sort=False, axis=1)
    # print(constructDf)
# print(constructTrainDf)
constructTrainDf.to_csv(constructedTrainPath, index=False, sep=",")
constructTestDf.to_csv(constructedTestPath, index=False, sep=",")
