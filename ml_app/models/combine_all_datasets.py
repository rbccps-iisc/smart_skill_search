import os
import pandas as pd
files = os.listdir("./output/")
csvs = []
for file in files:
    if file.endswith("csv"):
        csv = pd.read_csv(os.path.join("./output", file))
        csv = csv.drop(["id"], axis=1)
        csvs.append(csv)
df = pd.concat(csvs, axis=0, ignore_index=False)
df.to_csv("./output/combined.csv", index_label="id")