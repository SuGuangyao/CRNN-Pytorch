import  config
import os
path = "../data/labels"
file_names = os.listdir(path)
for fn in file_names:
    f = open(path+"\\"+fn,"r")
    with open(path + "\\" +'1'+fn, "w") as f1:
        fc = f.readlines()
        for line in fc:
            line =line.replace("D:\TMP\CRNN/data","../data")
            line = line.replace("\\", "/")
            f1.writelines(line)

        f1.close()
