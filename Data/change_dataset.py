import os
from process_file import each_file


folder_path = 'C:/Users/stahp/OneDrive/Documents/traffic signs3.0.v6i.yolov5pytorch'
folder_path += '/valid/labels'
files = os.listdir(folder_path)
for file in files:
    path = folder_path + '/' + file
    each_file(path)
    print(path)

