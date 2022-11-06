import pandas as pd
import numpy as np
import os
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

filepath = '../DataPre/data/train/feature.csv'
labelPath = '../DataPre/data/train/label.csv'
df = pd.read_csv(filepath)
label_df = pd.read_csv(labelPath)
df = df.fillna(0)
df = df.drop("APPLICATION_ID", axis=1)
print(df.head(5))
data = np.array(df)
labels = np.array(label_df["DEFAULT_LABEL"])

# 测试特征的性质
data = np.transpose(data)
data = normalize(data)
pca = PCA(n_components=1000)
newData = pca.fit_transform(data)
# print(newData)

features = df.keys()
print(features)
print(type(features))