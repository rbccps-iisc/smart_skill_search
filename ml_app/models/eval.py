from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from knn_model import KNNRecommender


# Accuracy after masking
for mask_ratio in [0.05, 0.1, 0.2]:
    acc_arr = []
    precision_arr = []
    recall_arr = []
    for i in range(10):
        df = pd.read_csv("./datasets/resumes_pilot.csv")

        X_train, X_test, _, _ = train_test_split(df, df, test_size=0.3)

        X_train = X_train.drop(X_train.iloc[:, 0:1], axis=1)
        model = KNNRecommender()
        model.fit(X_train)

        X_test = X_test.drop(X_test.iloc[:, 0:1], axis=1)
        mask = (np.random.uniform(0, 1,X_test.shape) >= mask_ratio)
        X_test_masked = X_test * mask
        predicted = model.get_batch_recommendation(X_test_masked)

        acc = np.mean(np.mean(predicted == X_test))

        TP = np.sum(1*(predicted*np.array(X_test)))
        FN = np.sum(1*(1-predicted)*np.array(X_test))
        FP = np.sum(1*(predicted*(1-np.array(X_test))))
        precision = TP/(TP+FP)
        recall = TP/(TP+FN)
        precision_arr.append(precision)
        recall_arr.append(recall)

        # recall = 

        acc_arr.append(acc)
    print(mask_ratio)
    print("acc", np.mean(acc_arr))
    acc = np.mean(acc_arr)
    print("precision", np.mean(precision_arr))
    prec = np.mean(precision_arr)
    print("recall", np.mean(recall_arr))
    rec = np.mean(recall_arr)
    print("F1", 2*prec*rec/(prec+rec))