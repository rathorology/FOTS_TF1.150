import os
import glob

folder_list = [x[0] for x in os.walk('data')][1:]

for folder in folder_list:
    files = [file for file in glob.glob(str(folder) + '/*.png')]
    import shutil

    for i in files:
        shutil.move(i, 'data/' + str(folder.split('/')[1]) + '_' + str(i.split('/')[-1]))

