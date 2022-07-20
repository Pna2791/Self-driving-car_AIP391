import os

directory = "D:\Desktop\AIP391\Lane detection\data/traffic signs data/50x50 bboxs/"

for i in range(26):
    os.mkdir(directory+str(i))
