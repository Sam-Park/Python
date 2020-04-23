"""
Lesson 02: Load time series Data

before you can develop forecast models, you must load and work with your time series data.
Pandas provides tools to lead data in CSV format. In this lesson, you will download a 
standard time series dataset, load it in Pandas and explore it.
You can load a time series dataset as a Pandas Series and specify the header row at line
zero, as follows:
"""
from pandas import read_csv
series = read_csv('daily-total-female-births.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
print(series.head(20))
print(series.size)
print(series.shape)
print(series.query())