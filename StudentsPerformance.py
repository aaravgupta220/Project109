import csv
import statistics
import pandas as pd

reader = pd.read_csv("StudentsPerformance.csv")

reading_list = reader["reading score"].to_list()
writing_list = reader["writing score"].to_list()

#mean median mode for reading score and writing score

reading_mean = statistics.mean(reading_list)
reading_median = statistics.median(reading_list)
reading_mode = statistics.mode(reading_list)
reading_stdev = statistics.stdev(reading_list)
writing_mean = statistics.mean(writing_list)
writing_median = statistics.median(writing_list)
writing_mode = statistics.mode(writing_list)
writing_stdev = statistics.stdev(writing_list)

print("Mean, median and mode of reading score is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
print("Mean, median and mode of writing score is {}, {} and {} respectively".format(writing_mean, writing_median, writing_mode))

#1, 2 and 3 standard deviations for reading score 

reading_1_stdev_start, reading_1_stdev_end = reading_mean - reading_stdev, reading_mean + reading_stdev

reading_2_stdev_start, reading_2_stdev_end = reading_mean - (2 * reading_stdev), reading_mean + (2 * reading_stdev)

reading_3_stdev_start, reading_3_stdev_end = reading_mean - (3 * reading_stdev), reading_mean + (3 * reading_stdev)

#1, 2 and 3 standard deviation for rwriting score

writing_1_stdev_start, writing_1_stdev_end = writing_mean - writing_stdev, writing_mean + writing_stdev

writing_2_stdev_start, writing_2_stdev_end = writing_mean - (2 * writing_stdev), writing_mean + (2 * writing_stdev)

writing_3_stdev_start, wwriting_3_stdev_end = writing_mean - (3 * writing_stdev), writing_mean + (3 * writing_stdev)

# percentage of data within 1, 2, and 3 standard deviations of reading score

reading_list_of_data_within_1_stdev = [result for result in reading_list if result > reading_1_stdev_start and result < reading_1_stdev_end]

reading_list_of_data_within_2_stdev = [result for result in reading_list if result > reading_2_stdev_start and result < reading_2_stdev_end]

reading_list_of_data_within_3_stdev = [result for result in reading_list if result > reading_3_stdev_start and result < reading_3_stdev_end]

# percentage of data within 1, 2, and 3 standard deviations of writing score

writing_list_of_data_within_1_stdev = [result for result in writing_list if result > writing_1_stdev_start and result < writing_1_stdev_end]

writing_list_of_data_within_2_stdev = [result for result in writing_list if result > writing_2_stdev_start and result < writing_1_stdev_end]

writing_list_of_data_within_3_stdev = [result for result in writing_list if result > writing_3_stdev_start and result < writing_1_stdev_end]

# printing data for reading score and writing score (stdev)

print("{}% of data for reading score lies within 1st standard deviation".format(len(reading_list_of_data_within_1_stdev) * 100.0 / len(reading_list)))

print("{}% of data for reading score lies within 2nd standard deviation".format(len(reading_list_of_data_within_2_stdev) * 100.0 / len(reading_list)))

print("{}% of data for reading score lies within 3rd standard deviation".format(len(reading_list_of_data_within_3_stdev) * 100.0 / len(reading_list)))

print("{}% of data for writing score lies within 1st standard deviation".format(len(writing_list_of_data_within_1_stdev) * 100.0 / len(writing_list)))

print("{}% of data for writing score lies within 2nd standard deviation".format(len(writing_list_of_data_within_2_stdev) * 100.0 / len(writing_list)))

print("{}% of data for writing score lies within 3rd standard deviation".format(len(writing_list_of_data_within_3_stdev) * 100.0 / len(writing_list)))