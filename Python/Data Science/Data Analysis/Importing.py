from re import S
from IPython.core.display import display, HTML
from sqlalchemy import create_engine
import sqlite3
import pandas as pd
import csv

# reading data
# normal reading
with open('btc-market-price.csv', 'r') as fp:
    for index, line in enumerate(fp.readlines()):
        if index < 10: # read first 10 lines
            timestamp, price = line.split(',')
            print(f'{timestamp}: ${price}')

file = open('btc-market-price.csv', 'r')
paragraph = file.readlines()
for index, line in enumerate(paragraph):
    if index < 10:
        timestamp, price = line.split(',')
        print(f'{timestamp}: ${price}')
file.close()

# the csv module
with open('btc-market-price.csv', 'r') as fp:
    reader = csv.reader(fp)
    for index, (timestamp, price) in enumerate(reader):
        if index < 10:
            print(f'{timestamp}: ${price}')

with open('exam-review.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter='>')
    next(reader) # skip the header
    for index, values in enumerate(reader):
        if not values: # empty values
            continue
        fname, lname, age, math, french = values
        print(f'{fname} {lname} (age: {age}) got {math} in math and {french} in frech')


# read using pandas
df = pd.read_csv('btc-market-price.csv', header=None, na_values=['', '?', '-'], names=['timestamp', 'prices'], dtype={'prices': 'float'}, parse_dates=['timestamp'], index_col=[0]) # can also take a url

# saving the csv file
df.to_csv('output.csv')


# reading from a database
conn = sqlite3.connect('sakila.db')
cur = conn.cursor() # cursor object to execute sql queries against our database
cur.execute('SELECT * FROM customer')
results = cur.fetchall()
df = pd.DataFrame(results)
df.columns =['customer_id', 'order_id', 'first_name', 'last_name', 'database_url', 'product_id', 'shipping_id', 's', 'delivery']
cur.close()
conn.close()


# read_sql methods
# 1) read_sql_query
conn = sqlite3.connect('sakila.db')
df = pd.read_sql_query('SELECT * FROM customer', conn) # the same as default
print(df)
conn.close()
# 2) read_sql_table
engine = create_engine('sqlite:///sakila.db')
connection = engine.connect()
df = pd.read_sql_table('customer', con=connection) # shows the table of the query 
print(df)


# create tables to dataframes
conn = sqlite3.connect('sakila.db')
cur = conn.cursor()
cur.execute('SELECT * FROM customer')
results = cur.fetchall()
df = pd.DataFrame(results)
print(df)
cur.execute('DROP TABLE IF EXISTS employees2;')
df.to_sql('employees2', conn)
cur.execute('SELECT * FROM employees2')
results = cur.fetchall()
df = pd.DataFrame(results)
print(df)
cur.close()
conn.close()


# read HTML
html_string = '''
<table>
    <thead>
        <tr>
            <th>Order date</th>
            <th>Region</th>
            <th>Item</th>
            <th>Units</th>
            <th>Unit Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1/6/2016</td>
            <td>East</td>
            <td>Pencil</td>
            <td>56</td>
            <td>1.76</td>
        </tr>
        <tr>
            <td>1/8/2018</td>
            <td>Central</td>
            <td>Binders</td>
            <td>26</td>
            <td>15.76</td>
        </tr>
    </tbody>
</table>
'''
display(HTML(html_string))
dfs = pd.read_html(html_string)
dfs2 = dfs[0]


# reading excel files
df = pd.read_excel('sales.xlsx', index_col='Customer')
df2 = pd.read_excel('sales.xlsx', sheet_name='By Product') # access by sheet names
# the ExcelFile class
excelfile = pd.ExcelFile('sales.xlsx') # read the excel file
excelfile.sheet_names

products = excelfile.parse(sheet_name='By Product', index_col=[0], header=0) # access by sheet names through the parse method
customers = excelfile.parse(sheet_name='By Product-Customer', index_col=[0], header=0) # access by sheet names through the parse method

# saving excel files
# method 1
products.to_excel('output.xlsx', sheet_name='Products')
excelfile = pd.ExcelFile('output.xlsx') # read the excel file
excelfile.sheet_names
sales = pd.read_excel('output.xlsx')
# method 2 - allows for saving more than one sheet file
writer = pd.ExcelWriter('output.xlsx')
products.to_excel(writer, sheet_name='Products')
customers.to_excel(writer, sheet_name='Customers')
writer.save()
excelfile = pd.ExcelFile('output.xlsx') # read the excel file
excelfile.sheet_names
customers = pd.read_excel('output.xlsx', sheet_name='Customers')


# positioning data
# products.to_excel('output.xlsx', sheet_name='Products', startrow=1, startcolumn=1) # shifts data positioning from 0,0

