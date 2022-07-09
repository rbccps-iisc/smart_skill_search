import numpy as np
import pandas as pd
import argparse
import os
import joblib

from knn_model import KNNRecommender

argparser = argparse.ArgumentParser("Process recommendation and save it to disk!")
argparser.add_argument("--input-name","-I",type=str, required="True")
argparser.add_argument("--output-name","-O", type=str, required="True")

args = argparser.parse_args()
# print(args)
input_name = args.input_name
output_name = args.output_name

if not os.path.exists(input_name):
    print("Please enter valid input file path!")
    exit(1)

input_csv = pd.read_csv(input_name)
input_csv = input_csv.drop(input_csv.iloc[:,0:1], axis=1)
column_names = input_csv.columns.tolist()


model = KNNRecommender()
model.fit(input_csv)
batch_mtx = model.get_batch_recommendation(input_csv)

def generate_csv(mtx, input_df, csv_path):
    skill_list = list(input_df.columns[1:])
    print(skill_list)
    skills_result = []
    for i in range(mtx.shape[0]):
        skills = [x for idx,x in enumerate(skill_list) if mtx[i,idx] == 1]
        skills_result.append(skills)
    df = pd.DataFrame(range(1,len(skills_result)+1),columns=['id'])
    print(df)
    df['skills'] = skills_result
    df.to_csv(csv_path, index=False)

temp_arr = output_name.split(".")
temp_arr[-1] = "joblib"
save_name = ".".join(temp_arr)

model.save(save_name)

generate_csv(batch_mtx,input_csv, output_name)