import numpy as np
import pandas as pd

# null values
pd.isna(np.nan)
pd.isna(None)
pd.isnull(np.nan)
pd.isnull(None)
pd.notna(None)
pd.notna(3)
pd.notna(np.nan)
pd.notnull(None)
pd.notnull(3)
pd.notnull(np.nan)

# working with series and dataframes
pd.isnull(pd.Series([2, 0, np.nan]))
pd.notnull(pd.DataFrame({
    'Column A': [2, 0, np.nan],
    'Column B': [np.nan, 0, np.nan],
    'Column C': [2, 0, 5]
}))

# pandas operations with missing values
# series
pd.Series([2, 0, 3,np.nan]).count()
pd.Series([2, 0, 3,np.nan]).mean()
pd.Series([2, 0, 3,np.nan]).median()
pd.Series([2, 0, 3,np.nan]).describe()
pd.Series([2, 0, 3,np.nan]).sum()

# filtering missing data
s = pd.Series([1, 2, np.nan, 6, None, 5, 8, np.nan])
pd.isnull(s) # returns true or false of the objects
pd.isnull(s).sum() # no of null values
pd.notnull(s).sum() # no of non null values

# null values as arguments
s[pd.isnull] # the null values
s[pd.notnull] # the non null values
s[pd.notnull].sum() # the sum of the non null values

# simplified options
s.isnull()
s.isnull().sum()
s.notnull()
s.notnull().sum()
s[s.isnull()] # boolean expression; returns a column with atleast one null value
s[s.notnull()] # boolean expression; returns a column with no null value
s[s.notnull()].sum()

# dropping null values
s.dropna() # same as s[s.notnull()]

# dataframes
df = pd.DataFrame({
    'Column A': [2, 0, np.nan, 7],
    'Column B': [np.nan, 0, np.nan, 4],
    'Column C': [2, 0, 5, 1],
    'Column D': [None, np.nan, None, np.nan],
    'Column E': [2, 4, 5, 9]
})
# df.info()
df.isnull()
df.drop('<column>', axis=1, inplace=True) # drops the column specified. Axis has to be specified. Inplace parameter is used to avoid reassigning the df to the expression stated.
df.drop(columns='column') # drop the specified column
df.drop(index='row') # drop the specified column
df.dropna() # drops any row with atleast one null value. By default axis=0
df.dropna(axis=0) # drops any row with atleast one null value
df.dropna(axis=1) # drops any column with atleast one null value
df.dropna(axis='columns') # drops any column with atleast one null value

df.dropna(how='any') # drop the rows with any no of null values. the default setting
df.dropna(how='any', axis='columns')
df.dropna(how='all') # drop the rows with all no being null values.
df.dropna(how='all', axis='columns')
df.dropna(thresh=3) # keep the rows with atleast 3 non-null values
df.dropna(thresh=3, axis='columns') # keep the columns with atleast 3 non-null values

# filling null values
s = pd.Series([1, 2, 3, np.nan, None, 6])
s.fillna(0)
s.fillna(s.mean())
s.fillna(method='ffill') # forward fill
s.fillna(method='bfill') # backward fill 
df.fillna(method='ffill') # forward fill along the columns also default 
df.fillna(method='ffill', axis=0) # forward fill along the columns 
df.fillna(method='ffill', axis='columns') # forward fill across the rows
df.fillna(method='ffill', axis=1) # forward fill across the rows
df
df.fillna({'Column A': 0, 'Column B': 45, 'Column D': df['Column E'].mean()})

# checking if there are null values
s.isnull().any()
s.isnull().all()
s.isnull().sum() # sum of all null values in the data
pd.Series([True, False, True, True]).any() # any true
pd.Series([True, False, True, True]).all() # all true
pd.Series([False, False, False, False]).any() # any true
pd.Series([True, True, True, True]).all() # all true
pd.Series([1, 3, 5, np.nan]).isnull().any()
pd.Series([1, 3, 5, np.nan]).isnull().all()
pd.Series([1, 3, 5]).isnull().any()

# cleaning not-null values
df = pd.DataFrame({
    'Sex': ['M', 'F', 'D', '?'],
    'Age': [19, 49, 495,  0]
})
df['Sex'].unique()
df['Sex'].value_counts() # total number of counts for each unique item
df['Sex'].value_counts().sum() # total number of non null values in the column
df.value_counts().sum() # total number of non null rows in the dataframe
df['Sex'].replace({'D': 'F', '?': 'M'})
df.replace({
    'Sex': {
        'D': 'F',
        '?': 'M'
    },
    'Age': {
        495: 49,
        0: 1
    }
    
})
df
df[df['Age'] > 100]
df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10
df

# duplicates
ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy', 
    'Germany', 
    'Germany', 
    'Germany'
], index = [
    'Gerard Araud', 
    'Kim Darroch', 
    'Peter Westmacott',
    'Armando Varricchio', 
    'Peter Wittig', 
    'Peter Ammon',
    'Klaus Scharioth'
])
ambassadors.duplicated() # keeps the first duplicate item
ambassadors.duplicated(keep='last') # keeps the last duplicate item
ambassadors.duplicated(keep=False) # keeps no duplicate item all are returned as True(duplicate items)
ambassadors.drop_duplicates() # keeps first and drops other duplicates
ambassadors.drop_duplicates(keep='last') # keeps last and drops other duplicates
ambassadors.drop_duplicates(keep=False) # drops all duplicates

players =pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'Lebron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant'
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})
players.duplicated() # both columns have to match for duplicate to return true
players.duplicated(subset='Name') # duplicates for name column
players.duplicated(subset='Pos') # duplicates for pos column
players.duplicated(subset='Pos', keep='last')
players.drop_duplicates()
players.drop_duplicates(subset='Name')
players.drop_duplicates(subset='Pos', keep='last')

# string handling
# splitting columns
df = pd.DataFrame({
    'Data': [
        '1987_M_US      _1',
        '1998?_M_UK _1',
        '19?92_F_US   _2',
        '1970?_M_ IT_1',
        '1985_F_I T_2',
    ]
})

df
df['Data'].str.split('_') # splits our string at the given delimiter
df['Data'].str.split('_', expand=True) # splits our string and creates a new column for each split
df = df['Data'].str.split('_', expand=True)
df.columns = ['Year', 'Sex', 'Country', 'Children']
df['Year'].str.contains('\?')
df['Country'].str.contains('U')
df['Country'].str.strip() # removes white spaces at the end of the string
df['Country'] = df['Country'].str.replace(' ', '') # more efficient than strip as it handles spaces anywhere in the string
df['Year'] = df['Year'].str.replace('\?', '') # more efficient than strip as it handles spaces anywhere in the string
# print(df['Year'].str.replace(r'?P<year>\d{4}\?', lambda m: m.group('year'))) - it know completely nothing about this
df
df.loc[df['Country']=='US', 'Children']

pd.get_dummies(df['<column>'], drop_first=True) # converts continuous data into discrete data, drop_first is optional.
pd.concat(['<df>', '<column1>', '<column2>', '<column3>'], axis=1, inplace=True) # concat joins all our discrete and original data into our df
