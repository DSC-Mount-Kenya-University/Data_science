from os.path import dirname
import pandas as pd
import os

MAIN_DIR = dirname(os.path.abspath(__file__))

data_frame = pd.read_csv(MAIN_DIR + "/netflix_titles.csv")
# data_frame.drop(data_frame.index[[2,3,4,5,6,7,8]], inplace=True)
data_frame = data_frame[data_frame["type"] == "Movie"]
data_frame = data_frame.aggregate(["min"])
print(data_frame)
