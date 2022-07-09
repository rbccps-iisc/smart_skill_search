from knn_model import KNNRecommender
import pandas as pd
import joblib

recommender = KNNRecommender()


# Load dataset and remove index column
with open("./datasets/resumes_development.csv", "rb") as f:
    dataset = pd.read_csv(f)
    dataset = dataset.drop(dataset.iloc[:,0:1], axis=1)


X_train = dataset
model = KNNRecommender()
model.fit(X_train)
mtx = model.get_batch_recommendation(X_train)
print(mtx.shape)

def generate_csv(mtx,input_df,csv_path):
    skill_list = list(input_df.columns[1:])
    skills_result = []
    for i in range(mtx.shape[0]):
        skills = [x for idx,x in enumerate(skill_list) if mtx[i,idx] == 1]
        skills_result.append(skills)
    df = pd.DataFrame(range(1,len(skills_result)+1),columns=['id'])
    print(df)
    df['skills'] = skills_result
    df.to_csv(csv_path, index=False)

generate_csv(mtx, dataset, "output.csv")