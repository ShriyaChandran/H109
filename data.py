import csv
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("data.csv")
data = df["reading score"].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
standard_dev = statistics.stdev(data)

first_stdev_start, first_stdev_end = mean-standard_dev, mean+standard_dev
second_stdev_start, second_stdev_end = mean-(2*standard_dev), mean+(2*standard_dev)
third_stdev_start, third_stdev_end = mean-(3*standard_dev), mean+(3*standard_dev)

List_score_first_dev = [result for result in data if result>first_stdev_start and result<first_stdev_end]
List_score_second_dev = [result for result in data if result>second_stdev_start and result<second_stdev_end]
List_score_third_dev = [result for result in data if result>third_stdev_start and result<third_stdev_end]

print("Mean of this data is:" + str(mean))
print("Median of this data is: " + str(median))
print("Mode of this data is: " + str(mode))
print("Standard deviation of this data is: " + str(standard_dev))
print("{}% of data for reading score lies in 1 standard deviation".format(len(List_score_first_dev)*100.0/len(data)))
print("{}% of data for reading score lies in 2 standard deviation".format(len(List_score_second_dev)*100.0/len(data)))
print("{}% of data for reading score lies in 3 standard deviation".format(len(List_score_third_dev)*100.0/len(data)))
