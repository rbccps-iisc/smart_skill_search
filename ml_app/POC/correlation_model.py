import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("./datasets/resumes_pilot.csv")
dataset = dataset.drop(dataset.iloc[:,0:1], axis=1)


corr = dataset.corr()
corr_plot = plt.matshow(corr)
plt.colorbar(corr_plot)
plt.show()

# TODO
# Save the model, input a row, complete the row
"""
Sample Workflow

model = CorrelationModel()
model.fit(dataset)
output_row = model.predict(input_row)
"""