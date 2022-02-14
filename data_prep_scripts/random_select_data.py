import os
import random

new_dir = "/home/$USER/path/to/output/dir"
data_dir = "/path/to/all/data/files"

file_list = []

for file in os.listdir(data_dir):
    if file.endswith(".wav"):
        file_list.append(file)

num_to_select_ran = 600
random_item_list = random.sample(file_list, num_to_select_ran)

for i in os.listdir(data_dir):
    if i in random_item_list:
        print("Copying " + i + " to " + new_dir)
        print("cp " + data_dir + "/" + i + " " + new_dir + "/" + i)
        os.system("cp " + data_dir + "/" + i + " " + new_dir + "/" + i)
