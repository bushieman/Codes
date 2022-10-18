# load data, missing data, headers, dtypes
import csv
import numpy as np
import pandas as pd

## Method 1
# with open('spam.data', 'r') as file:
#     data = list(csv.reader(file, delimiter=','))
# data = np.asarray(data[1:], dtype=np.float32)
# print(data.shape)

## Method 2
# data = np.loadtxt('spam.data', delimiter=',', dtype=np.float32, skiprows=1)
# print(data.shape)

## Method 3
data = np.genfromtxt('spam.data', delimiter=',', dtype=np.float32, skip_header=1, missing_values=['whr', 'sghd', np.NaN], filling_values=10.0)
print(data.shape)

## Method 4
df = pd.read_csv('spam.data', sep=',', header=None, dtype=np.float32, skiprows=1, na_values=['whr', 'sghd'])
df = df.fillna(0.0)
data = df.to_numpy()
print(data.shape)

## round(data, number of d.p needed)
round(23.53566774346, 4)
