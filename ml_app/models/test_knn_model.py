from knn_model import KNNRecommender
import pandas as pd

recommender = KNNRecommender()


# Load dataset and remove index column
with open("./datasets/resumes_pilot.csv", "rb") as f:
    dataset = pd.read_csv(f)
    dataset = dataset.drop(dataset.iloc[:,0:1], axis=1)


X_train = dataset
model = KNNRecommender()
model.fit(X_train)
mtx = model.get_batch_recommendation(X_train)
print(mtx.shape)