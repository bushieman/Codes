import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('music.csv')

# create custom columns
df2 = pd.read_csv('music.csv', header=None)
df2.columns = ['Age', 'Gender', 'Music-Genre']

# similar properties to numpy and other pandas dataframes
df.shape
df.head()
df.tail()
df.size
df.values
df.dtypes.value_counts()

# more elaborate read_csv
df3 = pd.read_csv('music.csv', header=None, names=['Age', 'Gender', 'Genre'], index_col=0, parse_dates=True)
df3[['Genre']]
df3.loc[23]


# plotting
df.plot()
plt.show()
