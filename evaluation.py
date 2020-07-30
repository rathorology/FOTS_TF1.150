import pandas as pd
from difflib import SequenceMatcher
import numpy as np


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio() * 100


train = pd.read_csv("train_result.csv")
test = pd.read_csv("test_result.csv")

for frame in [train, test]:
    list_per = list()
    for idx, row in frame.iterrows():
        actual = row['number']
        pred = row['pred_number']
        try:
            percent = similar(actual, pred)
        except Exception as e:
            prercent = 0
            # print(pred)
        list_per.append(percent)

    print(np.average(list_per))
