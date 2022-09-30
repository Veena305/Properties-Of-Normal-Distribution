import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import csv
df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()

height_mean = statistics.mean(height_list)
height_median = statistics.median(height_list)
height_mode = statistics.mode(height_list)

print("Mean of height is {}".format(height_mean))
print("Median of height is {}".format(height_median))
print("Mode of height is {}".format(height_mode))

height_std_deviation = statistics.stdev(height_list)

height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

fig = ff.create_distplot([height_list], ["MEAN"], show_hist=False)
fig.add_trace(go.Scatter(x=[height_mean, height_mean], y=[0, 0.22], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[height_first_std_deviation_start, height_first_std_deviation_start], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[height_first_std_deviation_end, height_first_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
fig.show()

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))