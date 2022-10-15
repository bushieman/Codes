# create a df pivot table
df = pd.pivot_table(df, index=df.index.month, columns=df.index.year, aggfunc='sum')
df.columns = df.columns.droplevel() # remove the double header (0) as pivot creates a multiindex.

# create a dataframe
df = pd.DataFrame('conditions')

# read csv file
pd.read_csv('path to file') 

# read excel file
pd.read_excel('path to excel file')

# creating mutiple indexes
pd.multiindex.from_arrays(arrays, names=('ondex1', 'index2')) 

# create a range of dates
pd.date_range(start='date1',
              periods=5,
              Freq='7D' or 'M' or '2Y')

# datetime
pd.to_datetime(df.col, format='%M').dt.month_name().str.slice(stop=3)

# numeric
pd.to_numeric(df.col)
