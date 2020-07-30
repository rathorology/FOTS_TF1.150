
import pandas as pd
import cv2

df = pd.read_csv("ground_truth.csv")
new = pd.DataFrame()
for idx, row in df.iterrows():
    name_img = str(df.iloc[idx][0].split('/')[0]) + '_' + str(df.iloc[idx][0].split('/')[1])
    name = str(name_img.split('.')[0]) + '.txt'
    number = str(df.iloc[idx][1])
    img = cv2.imread("data/" + name_img)
    y, x, c = img.shape
    text_file = open("annotation/gt_" + name, "w")
    text_file.write(
        '0,0' + ',' + str(x) + ',' + '0' + ',' + str(x) + ',' + str(y) + ',' + '0,' + str(y) + ',' + number)
    text_file.close()
