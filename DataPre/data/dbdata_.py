import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA


def plot2D(data):
    X = data[:, 0]
    Y = data[:, 1]
    T = np.arctan2(Y,X)
    plt.scatter(X,Y, s=75, c=T, alpha=.5)
    plt.show()

data_path = r".\train\feature.csv"
data = pd.read_csv(data_path)
data = data.drop("APPLICATION_ID", axis=1)
data = data.fillna(0)
data = np.transpose(data)

# normalized_data = data/np.linalg.norm(data)
normalized_data = normalize(data)
np.save('./normalized_data.npy', normalized_data)
normalized_data = np.load('./normalized_data.npy')
pca = PCA(n_components=2)
New_data = pca.fit_transform(normalized_data)
plot2D(New_data)

db = DBSCAN(eps=0.5, min_samples=5, metric='manhattan')
db.fit(normalized_data)
ids = db.labels_
mx = ids.max()
print(mx)
for i in range(mx + 1):
    print(np.sum(ids == i))
print(np.sum(ids == -1))

#print(ids)
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)
#print('Estimated number of clusters: %d' % n_clusters_)
#print('Estimated number of noise points: %d' % n_noise_)

