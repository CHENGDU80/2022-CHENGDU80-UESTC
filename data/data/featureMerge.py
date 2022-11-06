import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from tqdm import tqdm

def ConstructDataset(FilePath, outputPath, clusterDf):
    print("Reading " + FilePath + "...")
    originDf = pd.read_csv(FilePath)
    constructDf = pd.DataFrame()

    originDf = originDf.fillna(0)
    originDf = originDf.drop("APPLICATION_ID", axis=1)
    # print(originDf.head(5))
    # print(clusterDf.head(5))
    # print(constructDf)
    pca = PCA(n_components=1)
    for clusterID in tqdm(range(20)):
        tmpDf = pd.DataFrame()
        for _, row in clusterDf.iterrows():
            if row["Cluster"] == clusterID:
                # print(originDf[row["Feature"]])
                tmpDf = pd.concat([tmpDf, originDf[row["Feature"]]], sort=False, axis=1)
        tmpData = np.array(tmpDf)
        tmpData = normalize(tmpData)
        constructedData = pca.fit_transform(tmpData)
        # print(constructedData)
        tmpDf = pd.DataFrame(constructedData, columns=["f{0}".format(clusterID)])
        constructDf = pd.concat([constructDf, tmpDf], sort=False, axis=1)
        # print(constructDf)
    # print(constructTrainDf)
    constructDf.to_csv(outputPath, index=False, sep=",")

originTrainPath = "./train/feature.csv"
originTestPath = "./test/feature.csv"
clusterPath = "./cluster_out.csv"
constructedTrainPath = "./train/constructed_trainset.csv"
constructedTestPath = "./test/constructed_testset.csv"
clusterDf = pd.read_csv(clusterPath)
ConstructDataset(originTrainPath, constructedTrainPath, clusterDf)
ConstructDataset(originTestPath, constructedTestPath, clusterDf)