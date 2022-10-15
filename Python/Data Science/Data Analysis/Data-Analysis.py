from sqlalchemy import create_engine
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# read a csv file
sales = pd.read_csv('data.csv', parse_dates=['Date'])

# data characteristics
sales.head() # All columns, first 5 rows
sales.describe() # characteristics of the data e.g mean, median, max
sales.info() # shows the general info of our data 
sales.shape # returns a tuple of two values(x,y)
sales.size # shows the size of the data(x * y)

# reading specific columns
sales['Unit_Cost'].unique() # returns each unique values
sales['Unit_Cost'].unique().sum() # sum of all unique values
sales['Unit_Cost'].value_counts() # counts of all values
sales['Unit_Cost'].value_counts() # counts of each unique value in a series format
sales['Unit_Cost'].value_counts().sum() # sum of all counts. this is  the y of the shape same as the count method in describe

# plotting graphs
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(18,9))
sales['Unit_Cost'].plot(kind='density', figsize=(18,9))
sales['Unit_Cost'].value_counts().plot(kind='bar', figsize=(18,9))
sales['Unit_Cost'].value_counts().plot(kind='pie', figsize=(8,8))
sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(8,8))

# rltship btw columns
corr = sales.corr()
fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr.columns)), corr.columns)

# create new columns
sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']
sales['Revenue_per_Age'].describe()

# comparing columns
sales['Calculated_Cost'] = sales['Unit_Cost'] * sales['Order_Quantity']
(sales['Calculated_Cost']!=sales['Cost']).sum()

# increase unit price by 10%
sales['Unit_Price'].head()
sales['Unit_Price'] *= 1.1
sales['Unit_Price'].head()

# loc returns a group of rows and columns of the given condition
sales.loc[sales['State']=='Kentucky'] # all columns
sales.loc[sales['State']=='Kentucky', 'Revenue'] # specified column('Revenue')
sales.loc[sales['State']=='Kentucky', 'Revenue'].describe()

# mean revenue for adults 35-64 in the U.S
sales.loc[(sales['Age_Group']=='Adults (35-64)') & (sales['Country']=='United States'), 'Revenue'].mean()



# reading from a database
conn = sqlite3.connect('sakila.db')

df = pd.read_sql('''
SELECT 
    c.last_name AS customer_lastname, 
    cy.city AS rental_store_city, 
    f.rating AS film_rating,
    f.rental_duration AS film_rental_duration,
    f.rental_rate AS film_rental_rate,
    f.replacement_cost AS film_replacement_cost,
    f.title AS film_title, 
    r.rental_date,
    r.return_date, 
    r.rental_id,
    s.store_id
FROM rental r
JOIN customer c
	ON r.customer_id = c.customer_id
JOIN inventory i
	ON r.inventory_id = i.inventory_id
JOIN store s
	ON i.store_id = s.store_id
JOIN address a
	ON s.address_id = a.address_id
JOIN city cy
	ON a.city_id = cy.city_id
JOIN film f
	ON i.film_id = f.film_id
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])

# check if database is connected
df.head()
df.shape

# read_sql methods
# 1) read_sql_query
df = pd.read_sql_query('<queries>', conn) # the same as default
# 2) read_sql_table
engine = create_engine('sqlite:///sakila.db')
connection = engine.connect()
df = pd.read_sql_table('<table>', con=connection) # the same as default



# graphs
ax = df['film_rental_rate'].value_counts().plot(kind='bar', figsize=(16,8))
ax.set_ylabel('Number of Rentals')

# value count method
df['rental_store_city'].describe() # when you see uniques in this method you should use the value_counts method to access the basic describe functions
df['rental_store_city'].value_counts().describe()

# Question 1: The rental_gain_cost formula is given as; rental_gain_cost = film_rental_rate / film_replacement_cost * 100.
# A.) Calculate the rental_gain_cost mean to 2 decimal places
df['rental_gain_cost'] = df['film_rental_rate'] / df['film_replacement_cost'] * 100
df['rental_gain_cost'].mean().round(2)
# B.) Draw the mean, median lines
ax = df['rental_gain_cost'].plot(kind='density', figsize=(18,9))
ax.axvline(df['rental_gain_cost'].mean(), color='red')
ax.axvline(df['rental_gain_cost'].median(), color='green')

# Question 2: How many PG or PG-13 rating films were rented?
df.loc[(df['film_rating']=='PG') | (df['film_rating']=='PG-13')].shape[0]

# Question 3: Create a list of all the films with the highest replacement cost
df.loc[df['film_replacement_cost']==df['film_replacement_cost'].max(), 'film_title'].unique() # unique means without repeating

plt.show()
