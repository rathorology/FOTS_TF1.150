import collections

import pandas as pd
import glob
import operator
from numpy import loadtxt


def PolygonArea(corners):
    n = len(corners)  # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

not_found =list()
df = pd.read_csv("ground_truth.csv")
result = pd.DataFrame()
files = [file for file in glob.glob('outputs/' + '*.txt')]
for f in files:
    org_name = f.split('/')[1]
    org_name = org_name.split('_')[1:]
    org_name = "_".join(org_name)
    org_name = org_name.split('.')[0] + '.png'

    try:
        data = pd.read_csv(f, header=None)
    except Exception as e:
        not_found.append(0)
        # print(org_name)
        # print('=================================================================================')
        continue
    col = data.columns
    if data.shape[0] == 2:
        post = data.iloc[0][col[-1]]
        pre = data.iloc[1][col[-1]]

        number = pre + post
        s = df[df['name'] == org_name]

        result = result.append({
            "name": s['name'].tolist()[0],
            "number": s['number'].tolist()[0],
            "pred_number": number
        }, ignore_index=True)


    elif data.shape[0] > 2:
        dit = dict()
        for idx, row in data.iterrows():
            corners = [(row[0], row[1]), (row[2], row[3]), (row[4], row[5]), (row[6], row[7])]
            a = PolygonArea(corners)
            dit[idx] = a
        dit = sorted(dit.items(), key=operator.itemgetter(1))
        index = [dit[-2:][0][0], dit[-2:][1][0]]
        data = data.iloc[index, :]

        pre = data.iloc[0][col[-1]]
        post = data.iloc[1][col[-1]]

        number = pre + post
        s = df[df['name'] == org_name]
        result = result.append({
            "name": s['name'].tolist()[0],
            "number": s['number'].tolist()[0],
            "pred_number": number
        }, ignore_index=True)

    else:
        print(org_name)
        not_found.append(0)
        print(data.iloc[0][col[-1]])
        print('=====================================================================================')

print(len(not_found))
# result.to_csv('train_result.csv', index=False)
# result.to_csv('test_result.csv', index=False)
