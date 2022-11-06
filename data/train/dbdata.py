import pandas as pd
import numpy as np
import math as mt
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.cluster import KMeans
data_path = r"C:\Users\22259\Desktop\chengdu80\UESTC\data\train\feature.csv"
data = pd.read_csv(data_path)
data = data.drop("APPLICATION_ID", axis=1)
data = data.fillna(0)
#print(data)
new_data = preprocessing.normalize(data)
#print(New_data)

new_data = np.transpose(new_data)
#db = DBSCAN(eps=0.5, min_samples=5,metric='manhattan')
kmeans = KMeans(n_clusters=40, random_state=0).fit(new_data)
ids = kmeans.labels_
mx = np.max(ids)
#fp=open(r'.\ids.txt', 'w')
#print("end2")
#print(ids,file=fp)
for i in range(0,mx+1):
    print(np.sum(ids == i))
print(np.sum(ids == -1))
#print(ids)
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)
#print('Estimated number of clusters: %d' % n_clusters_)
#print('Estimated number of noise points: %d' % n_noise_)

