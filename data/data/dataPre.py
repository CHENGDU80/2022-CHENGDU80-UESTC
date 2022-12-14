import pandas as pd
import numpy as np
import os
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

filepath = "train/constructed_trainset.csv"
labelPath = "train/label.csv"
df = pd.read_csv(filepath)
labeldf = pd.read_csv(labelPath)
# df = df.fillna(0)
# df = df.drop("APPLICATION_ID", axis=1)
print(df.head(5))
data = np.array(df)
labels = np.array(labeldf["DEFAULT_LABEL"])
print(len(labels))
print(len(df))
#data = normalize(data)
# pca = PCA(n_components=1000)
# newData = pca.fit_transform(data)
# print(newData)

features = df.keys()
print(features)
print(type(features))
if os.path.exists("new_importances4.npy"):
    importances = np.load("new_importances4.npy")
else:
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(data, labels, test_size=0.3, train_size=0.7)
    rf = RandomForestClassifier(n_estimators=100,max_depth=None)
    rf.fit(Xtrain, Ytrain)
    importances = rf.feature_importances_
    print(importances)
    print("ALreaddy out")
    np.save(file="new_importances4", arr=importances)
indices = np.argsort(importances)[::-1]
saveDF = pd.DataFrame(columns=["Feature", "Importance"])
for f in range(20):
  #  saveDF = pd.concat([saveDF,{"Feature":features[indices[f]], "Importance":importances[indices[f]]}], ignore_index=True)
    saveDF = saveDF.append({"Feature":features[indices[f]], "Importance":importances[indices[f]]}, ignore_index=True)
    print("%2d) %-*s %f" % \
          (f + 1, 30, features[indices[f]], importances[indices[f]]))
saveDF.to_csv("new_importances4.csv", index=False, sep=",")
