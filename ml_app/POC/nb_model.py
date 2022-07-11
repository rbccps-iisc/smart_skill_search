import pandas as pd
from regex import X
from sklearn.model_selection import train_test_split
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

model = OneVsRestClassifier(BernoulliNB())
model.fit(X_train, y_train)
predicted = model.predict(X_test)
# print(predicted == y_test)

acc = np.mean(np.mean(predicted == y_test))
print(acc)
# print(X_train.T)

n_cols = X_test.shape[-1]
# np.array(X_test.iloc[:, 3])
# print(y_test.iloc[:, 3])
# auc_score = [ auc(np.array(X_test.iloc[:,i]), np.array(predicted[:,i])) for i in range(n_cols)]

# print(auc_score)

# y = np.array([1, 1, 2, 2])
# pred = np.array([0.1, 0.4, 0.35, 0.8])
# for i in range(n_cols):
#     fpr, tpr, thresholds = sklearn.metrics.roc_curve(y, pred, pos_label=2)
#     print(sklearn.metrics.auc(fpr, tpr))

