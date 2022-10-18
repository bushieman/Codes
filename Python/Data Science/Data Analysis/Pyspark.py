import pyspark

# creating a spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Dataframe').getOrCreate()

# reading a dataframe
df = spark.read.csv('Top_100_buildings_under_construction.csv', header=True, inferSchema=True)

df.show() # show the df: always call the .show() method when you want to view the any instance of the df 
# e.g in dropping cols, creating cols, selecting cols, modifying cols
df.head() # accessing the df
df.printSchema() # show df info
df.dtypes # show df dtypes
df.describe().show() # show the df describe info
df.columns # show df cols

# selecing columns
df.select('NAME') # single col
df.select(['NAME', 'HEIGHT']) # multiple cols

# creating new columns
df.withColumn('colName', 'data')

# dropping columns
df.drop('MATERIAL')# single col
df.drop(['MATERIAL', 'FUNCTION'])# multiple cols

# manipulating columns
df['HEIGHT'] + 2
df['HEIGHT'] * 2
df['HEIGHT'].apply() # ??

# renaming the columns
df.withColumnRenamed('existing', 'new')

# handling missing values
# dropping missing values
df.na.drop() # drop any row with atleast one null value
df.na.drop(how='any or all') # drop any=atleast one null value, all=all values should be null
df.na.drop(thresh=3) #  drop any row with 2 non-null values or less
df.na.drop(subset=['MATERIAL']) # drop any null value across any row but only in the MATERIAL column
df.na.drop(subset=['MATERIAL', 'COMPLETION'])

# filling missing values
df.na.fill('value') # fill null values with the specified value
df.na.fill('value', 'COMPLETION') # fill null values with the specified value in a specific subset i.e specific column
df.na.fill('value', ['COMPLETION', 'MATERIAL']) # specific subsets

# replacing missing values
df.na.replace('col to replace', 'value') # replace any null value with the value in the specified cols

# filter operations: <, >, ==, <=, >=, &, |, ~
df.filter('condition') # name given should be in df cols
df.filter('FLOORS>50') # df where discourse_start > 200
df.filter(df['FLOORS']>50) # same filter operation as line above
df.filter((df['FLOORS']>50) & (df['MATERIAL'] == 'composite')).select(['NAME', 'CITY', 'COMPLETION']) # return NAME, CITY & COMPLETION cols where the conditions are True
df.filter(df['FLOORS'] in range(50, 100)) # buildings ranging between 50 and 100 floors

# GroupBy and Aggregate functions
df.groupBy('CITY').sum() # groupby CITY and return sum of int cols i.e FLOORS, COMPLETION
df.groupBy('CITY').mean() # mean of FLOORS, COMPLETION per CITY
df.groupBy('CITY').count() # no of buildings in every city
df.groupBy('NAME').max('HEIGHT') # groupby tallest building
df.groupBy('NAME').min('HEIGHT') # groupby shortest building
df.groupBy('CITY').max('HEIGHT') # groupby city with the most construction in terms of metres covered vertically
df.groupBy('CITY').agg({'CITY': 'count', 'COMPLETION': 'mean', 'FLOORS': 'sum'})


