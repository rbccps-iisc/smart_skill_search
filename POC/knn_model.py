import pandas as pd
from regex import X
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
from sklearn.metrics import auc
from sklearn.naive_bayes import BernoulliNB
import sklearn.metrics

with open("./datasets/resumes_pilot.csv", "rb") as f:
    dataset = pd.read_csv(f)
    dataset = dataset.drop(dataset.iloc[:,0:1], axis=1)
    print(dataset.head())

X_train, X_test, y_train, y_test = train_test_split(dataset, dataset, test_size=0.3)

# print(len(X_train), len(X_test))
model_knn = NearestNeighbors(metric=sklearn.metrics.hamming_loss)
model_knn.fit(X_train)


class KNNRecommender:
    def __init__(self):
        self.model_knn = NearestNeighbors(metric=sklearn.metrics.hamming_loss)
    def fit(self, X):
        self.model_knn.fit(X)
        self.X = X
    def recommend(self, row):
        dist, indices = self.model_knn.kneighbors([row])
        rec_matrix = np.array([self.X.iloc[idx] for idx in indices])
        print(rec_matrix)
        print(indices)
        return rec_matrix

model = KNNRecommender()
model.fit(X_train)
rec = model.recommend(X_train.iloc[0]).squeeze()
print(rec.shape)
threshold = 1
rec_add = 1*(rec.sum(axis=0) > threshold)
print(rec_add == np.array(X_train.iloc[0]))
np.savetxt("rec.txt", rec.squeeze().astype(np.int8))
