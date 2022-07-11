"""Recommender system implemented using KNN"""
from __future__ import annotations

import joblib
from sklearn.neighbors import NearestNeighbors
import numpy as np
from tqdm import tqdm
import pandas as pd


class KNNRecommender:
    def __init__(self, k=5, threshold=2):
        """
        Recommender system implemented using Nearest Neighbours algorithm

        Parameters
        ----------
        k : int, deafult=5
            Number of nearest neighbors.

        threshold : int, default=2
            The threshold used for determining if the user posses a possible skill.
        """
        self.model_knn = NearestNeighbors(
            metric="manhattan", n_neighbors=k)  # manhattan distance is equivalent to hamming distance when the data is unary.
        self.k = k
        self.threshold = threshold

    def fit(self, X: pd.DataFrame):
        """
        Fits the dataset to the recommender.

        Parameter
        ---------
        X : pandas dataframe
            The dataset to be fitted.
        """
        self.model_knn.fit(X.values)
        self.X = X

    def recommend(self, row: np.ndarray) -> np.ndarray:
        """
        This function outputs suggestion as a binary array.

        Parameters
        ----------
        row : np.ndarry
            The binary array denoting mention of a skill is denoted by 1.

        Returns
        -------
        recommendation: np.ndarray
            The binary array of possible skills.
        """
        dist, indices = self.model_knn.kneighbors([row])
        rec_matrix = np.array([self.X.iloc[idx] for idx in indices]).squeeze()
        row = np.array(row).reshape(1, -1).astype(float)
        rec_matrix = np.concatenate([rec_matrix, row*self.threshold], axis=0)

        recommendation = 1 * \
            (rec_matrix.squeeze().sum(axis=0) >= self.threshold)
        return recommendation

    def get_batch_recommendation(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predicts possible skills for all users in a dataset.

        Parameter
        ---------
        X : pandas dataframe
            The dataset to which recommenders to be generated.

        Returns
        -------
        recommendations: np.ndarray
            The recommendations for all rows in X.
        """
        batch = []
        for row in tqdm(X.iterrows(), total=len(X)):
            batch.append(self.recommend(row[1]))
        recommendations = np.array(batch)
        return recommendations

    def save(self, filename: str) -> None:
        """
        Saves the model to the disk.

        Parameter
        ---------
        filename: str
            The file name for the model to be saved.
        """
        joblib.dump(self, filename)

    def load(self, filename: str):
        """
        Loades the trained model from the disk.

        Parameter
        ---------
        filename: str
            The file name for the model to be loaded.
        """
        self = joblib.load(filename)
