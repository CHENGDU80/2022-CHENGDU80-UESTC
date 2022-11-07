import pandas as pd
import numpy as np
import math as mt
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
data_path = r"constructed_trainset-20.csv"
data = pd.read_csv(data_path)
# #print(data)
#new_data=np.load('cos_data.npy')

# new_data=np.transpose(data)


# cos_data =cosine_similarity(new_data, new_data)
# np.save(r"cos_data",cos_data)
# exit()
#
db = DBSCAN(eps=0.08, min_samples=5,metric='cosine')
ids = db.fit(data).labels_
#kmeans = KMeans(n_clusters=30, random_state=0).fit(new_data)
#ids = kmeans.labels_

#ids, error, nfound = kcluster(new_data,  nclusters=20, dist='u', npass=100)
mx = np.max(ids)
fp=open('.\ids.txt', 'w')
print(ids,file=fp)
for i in range(0,mx+1):
    print(np.sum(ids == i))
print(np.sum(ids == -1))
#print(ids)
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)
#print('Estimated number of clusters: %d' % n_clusters_)
#print('Estimated number of noise points: %d' % n_noise_)

