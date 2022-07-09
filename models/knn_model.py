from sklearn.neighbors import NearestNeighbors
import numpy as np
from tqdm import tqdm

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
            batch.append(self.recommend(row[1]))
        return np.array(batch)