import os, sys

file_list = os.listdir("./")

f = open("train.txt", 'w')
for i in file_list:
    if ".jpg" in i:
        data = "./{}\n".format(str(i))
        f.write(data)
f.close()

print('[INFO] The List of jpg files is written in "train.txt"')