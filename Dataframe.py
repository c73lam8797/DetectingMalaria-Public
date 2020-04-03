import pandas as pd
import numpy as np
import glob
import csv
from random import random

# data = pd.read_csv("C:\\Users\\charm\\Documents\\GitHub\\ML\\MURA-v1.1\\train_labeled_studies.csv") #returns a data frame 
# data["PATHS"]=data["PATHS"].astype(str)
# data["VAL"]=data["VAL"].astype(str)


f = open("C:\\Users\\charm\\Documents\\GitHub\\MalariaML\\infected_rand.csv", "w", newline="")

path="C:\\Users\\charm\\Documents\\GitHub\\MalariaML\\cell-images-for-detecting-malaria\\cell_images\\Parasitized"
tempFiles = glob.glob(f"{path}/*.png")

writer = csv.writer(f)
for path in tempFiles:
    writer.writerow([path, 1, random()])

path="C:\\Users\\charm\\Documents\\GitHub\\MalariaML\\cell-images-for-detecting-malaria\\cell_images\\Uninfected"
tempFiles = glob.glob(f"{path}/*.png")

writer = csv.writer(f)
for path in tempFiles:
    writer.writerow([path, 0, random()])


# f.close()

# data.info()
# print(f"Number of 0s: {num[0]}")
# print(f"Number of 1s: {num[1]}")
# print (f"Percentage of 1s: {(num[1]/(num[0]+num[1])*100)}")

# data = pd.read_csv("C:\\Users\\charm\\Documents\\GitHub\\ML\\MURA-v1.1\\test_labeled_image_file_paths-Copy.csv") #returns a data frame 

# num = {0:0, 1: 0}

# for val in data["VAL"]:
#     if (val==0):
#         num[0] += 1
    
#     if (val==1):
#         num[1] += 1


# print(f"Number of 0s: {num[0]}")
# print(f"Number of 1s: {num[1]}")
# print (f"Percentage of 1s: {(num[1]/(num[0]+num[1])*100)}")

