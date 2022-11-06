import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from imblearn.over_sampling import SMOTE
from tqdm import tqdm
from collections import Counter

def ConstructDataset(FilePath, outputPath, clusterDf):
    print("Reading " + FilePath + "...")
    originDf = pd.read_csv(FilePath)
    constructDf = pd.DataFrame()

    originDf = originDf.fillna(0)
    if "APPLICATION_ID" in originDf.columns:
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
trainLablePath = "./train/label.csv"
enhancedTrainPath = "./train/enhanced_feature_3_1.csv"
enhancedTrainLabelPath = "./train/enhanced_feature_label_3_1.csv"

originTestPath = "./test/feature.csv"
clusterPath = "./cluster_out.csv"
constructedTrainPath = "./train/constructed_trainset.csv"
constructedTestPath = "./test/constructed_testset.csv"
clusterDf = pd.read_csv(clusterPath)

if not os.path.exists(enhancedTrainPath) and not os.path.exists(enhancedTrainLabelPath):
    df = pd.read_csv(trainLablePath)
    print(Counter(df["DEFAULT_LABEL"]))
    trainDf = pd.read_csv(originTrainPath).drop("APPLICATION_ID", axis=1)
    trainDf = trainDf.fillna(0)
    smo = SMOTE(random_state=111, sampling_strategy = {1:23985})
    newTrainDf, labelDf = smo.fit_resample(trainDf, df["DEFAULT_LABEL"])
    print(Counter(labelDf))
    print(newTrainDf)
    print(labelDf)
    newTrainDf.to_csv(enhancedTrainPath, index=False, sep=",")
    labelDf.to_csv(enhancedTrainLabelPath, index=False, sep=",")
ConstructDataset(enhancedTrainPath, constructedTrainPath, clusterDf)
# ConstructDataset(originTestPath, constructedTestPath, clusterDf)