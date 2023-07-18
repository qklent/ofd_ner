import pandas as pd
from preprocess_data import preprocess_string
import os

PATH_TO_DATA = "../data/train_supervised_dataset.csv"


data = pd.read_csv(PATH_TO_DATA)[:5]
print("init_data:")


for x in data.name:
    print (x)

preprocessed_data = list(map(preprocess_string, data.name))
print("\n\npreprocessed_data:")

for x in preprocessed_data:
    print(x)