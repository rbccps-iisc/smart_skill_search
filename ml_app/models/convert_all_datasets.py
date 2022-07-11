import os
files = os.listdir("./datasets/")
for file in files:
    if file.endswith("csv"):
        input_path = os.path.join("./datasets/", file)
        output_path = os.path.join("./output/", file)
        command = f"python3 create_batch_recommendation.py -I'{input_path}' -O'{output_path}'"
        print(command)
        os.system(command)
