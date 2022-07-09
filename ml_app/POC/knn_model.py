import pandas as pd
from regex import X
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
from sklearn.metrics import auc
from sklearn.naive_bayes import BernoulliNB
import sklearn.metrics
from tqdm import tqdm

with open("./datasets/resumes_pilot.csv", "rb") as f:
    dataset = pd.read_csv(f)
    dataset = dataset.drop(dataset.iloc[:,0:1], axis=1)
    print(dataset.head())

X_train, X_test, y_train, y_test = train_test_split(dataset, dataset, test_size=0.3)

# print(len(X_train), len(X_test))
model_knn = NearestNeighbors(metric=sklearn.metrics.hamming_loss)
model_knn.fit(X_train.values)


class KNNRecommender:
    def __init__(self, k=5, threshold=2):
        self.model_knn = NearestNeighbors(metric="manhattan", n_neighbors=k)
        self.k = k
        self.threshold = threshold
    def fit(self, X):
        self.model_knn.fit(X.values)
        self.X = X
    def recommend(self, row):
        dist, indices = self.model_knn.kneighbors([row])
        rec_matrix = np.array([self.X.iloc[idx] for idx in indices])
        recommendation = 1 * (rec_matrix.squeeze().sum(axis=0) > self.threshold)
        return recommendation

    def get_batch_recommendation(self, X):

        batch = []
        idx = 0
        for row in tqdm(X.iterrows(), total = len(X)):
            idx += 1
            batch.append(self.recommend(row[1]))
        return np.array(batch)

    

model = KNNRecommender()
model.fit(X_train)
mtx = model.get_batch_recommendation(X_train)
# # print(batch.shape)
# print(mtx.shape)
# # rec = model.recommend(X_train.iloc[0]).squeeze()
# # print(rec.shape)
# # threshold = 1
# # rec_add = 1*(rec.sum(axis=0) > threshold)
# # print(rec_add == np.array(X_train.iloc[0]))
# # np.savetxt("rec.txt", rec.squeeze().astype(np.int8))
