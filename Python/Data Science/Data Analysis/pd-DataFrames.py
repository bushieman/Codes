import pandas as pd

# creating dataframes
# manually
df = pd.DataFrame({
    'Population': [34.244,63.951, 80.94, 60.665, 127.061, 54.511, 318.523],
    'GDP': [
        1785387,2833687,3874437,2167744,4602367,2950039,17348075
    ],
     'Continent': [
        'America', 'Europe', 'Europe', 'Europe','Asia', 'Europe', 'America'
    ],
    'Surface Area': [
        9984670,640679,357114,301336,377930,242495,9525067
    ],
    'HDI': [
        0.912,0.888,0.916,0.873,0.891,0.907,0.915
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

df.index = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']

# attributes
df.columns
df.index
# df.info()
df.size
df.shape
df.describe()
df.dtypes
df.dtypes.value_counts()

# indexing, selection and slicing
df['Population'] # access the columns specified. Works on the column-level
df['Population'].to_frame() # pd series to dataframe
df[['GDP']] # a alternative to to_frame()
df[['GDP', 'Population']] # mulitple series to dataframe
df[1:3] # slicing creates another dataframe. It's unique to np as it acts on row-level
df.loc['Canada'] # loc selects rows matching the given index
df.iloc[0] # iloc selects rows matching the sequencial index
df.iloc[[0, 1, -1, -2]]
df.iloc[0:3]
df.iloc[0:3, 3] # the second 3 specifyes the column at index 3
df.iloc[0:3, [1, 3]] # [1, 3] - take the columns between index 1 and 3 including 3 
df.iloc[0:3, 0:3] # rows at index 0, 1, 2, columns at index 0, 1, 2
df.loc['Canada':'Italy']
df.loc['Canada':'Italy', 'Population']
df.loc[:, ~df.columns.duplicated()] # select all rows, select all columns except for duplicated columns
df.loc['Canada':'Italy', ['Population', 'Surface Area']]
df.loc[df['Population']>70, ['Population']] # loc can also take conditions
df.loc[df['Population']>70, ['Population', 'GDP']]

# dropping stuff - does not change the original dataframe until you use the inplace=True parameter
df.drop('Canada')
df.drop(['Canada', 'Japan'])
df.drop(['Canada', 'Japan'], axis=0)
df.drop(['Canada', 'Japan'], axis='rows')
df.drop(columns=['Population', 'HDI'])
df.drop(['Population', 'HDI'], axis=1)
df.drop(['Population', 'HDI'], axis='columns')

# operations with series work at a column level
# workout the GDP and the HDI of the g-7 countries after the covid-19 crisis
df[['GDP', 'HDI']]
crisis = pd.Series([-1_000_000, -0.3], index=['GDP', 'HDI'])
crisis
df[['GDP', 'HDI']] + crisis

# modifying dataframes
languages = pd.Series(['English-US', 'French', 'German', 'Italian', 'Mandarin', 'English-UK', 'English-US'], 
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States'],
    name='Languages'
)
df['Languages'] = languages
df['Languages'] = 'English' # modify all languages to English
df.rename(columns={
    'GDP': 'Gross Domestic Product',
    'HDI': 'Human Development Index'
}, index={
    'United Kingdom': 'UK',
    'United States': 'US'
})
# calculate the GDP Per Capita and add it to the dataframe
df['GDP Per Capita'] = df['GDP'] / df['Population']

# other statistical info
population = df['Population']
print(population.sum())
print(population.median())
print(population.quantile(.25))
print(population.quantile([.3, .90, 1]))
print(len(population))
df.Population.astype(str) # change the type of the dataframe object
df.dtypes # check the type of the dataframe columns
df.Population.dtype # check the type of the dataframe column

# merging
df.merge(df2, on=['column_1', 'column_2'], how='left')

# display
display(df) # display all dataframes in one cell output

df.query('query by specified query inside the string') # querying
