import pandas as pd
import numpy as np
import math as mt
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
data_path = r"C:\Users\22259\Desktop\chengdu80\UESTC\data\train\feature.csv"
data = pd.read_csv(data_path)
data = data.drop("APPLICATION_ID", axis=1)
data = data.fillna(0)

pca = PCA(n_components=1000)
New_data = pca.fit_transform(data)
New_data = np.transpose(New_data)
db = DBSCAN(eps=0.05, min_samples=5)
db.fit(New_data)
ids = db.labels_
mx = ids.max()
print(mx)
for i in range(1,mx):
    print(np.sum(ids == i))
print(np.sum(ids == -1))
#print(ids)
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)
#print('Estimated number of clusters: %d' % n_clusters_)
#print('Estimated number of noise points: %d' % n_noise_)

