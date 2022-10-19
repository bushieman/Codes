-- MySQL uses Relational DB'S ie multiple tables related to each other using a relationship.
-- we use semi-colon to separate multiple queries

-- the USE clause selects the database to use
USE sql_store;
-- Note: MySQL is not case sensitive, we only use casing to make the syntax muc pretier
-- the SELECT clause with * selects every column from customers table
-- the FROM  clause references the target table
SELECT * 
FROM customers;

-- you can avoid the USE clause with the following syntax
SELECT * FROM sql_store.customers

-- selects specific columns from customers table explicitly
SELECT customers_id, first_name
FROM customers;

-- you can use arithmetic expressions on columns
SELECT points*100+34 FROM customers;

-- use an alias for your columns
SELECT
    points AS dollars
FROM customers;

-- for double names you can either use underscore to join the two names or surround them in a string
SELECT points AS 'Bank Balance', last_name as nick_name FROM customers;

-- use DISTINCT clause to select unique keywords
SELECT DISTINCT state >= From customers

-- the WHERE  clause filters data
SELECT *
FROM customers
WHERE points > 3000;

-- comparison operators
>, <, >=, <=, !=, <>, = -- <> represents not equal to

-- AND operator has a higher precedence than OR operator but can be overwritten by using parenthesis

-- the AND, OR operators
WHERE (birth_date > '1990-01-01' OR points > 1000) AND state = 'VA' -- also lowercase 'va' should work

-- the NOT operator
WHERE NOT(birth_date > '1990-01-01' OR points > 1000) -- Note: Dates are also represented as strings. Also take note of the syntax

-- the IN operator
WHERE state IN ('VA', 'NY', 'LA') -- simpler syntax to WHERE STATE = 'VA' OR STATE='NY' OR STATE='LA'

-- the NOT and IN syntax
WHERE state NOT IN ('VA', 'NY', 'LA')

-- the BETWEEN  operator
WHERE points BETWEEN 1000 AND 3000

-- the LIKE operator
WHERE last_name LIKE 'bush'

-- the NOT LIKE syntax
WHERE last_name NOT LIKE 'bush'

-- the % sign represents any number of characters after b
WHERE last_name LIKE 'b%'

WHERE last_name LIKE 'bush%' -- both bush and bushman are hits

-- the % represents a b somewhere inside the last_name ie any no of char before or after
WHERE last_name LIKE '%b%'

-- the % represents any number of characters before b
WHERE last_name LIKE '%b'

-- each underscore represents a character therefore the word is a three digit word ending with b
WHERE last_name LIKE '__b'

-- REGEXP clause
-- the REGEXP operator shows b is anywhere in the word
WHERE last_name REGEXP 'b'

-- the caret shows b is at the beginning of the word
WHERE last_name REGEXP '^b'

-- the caret shows b is at the end of the word
WHERE last_name REGEXP 'b$'

-- the pipe represents multiple search patterns 
WHERE last_name REGEXP 'bush|vera'

WHERE last_name REGEXP '^bush|mil|pen$' -- bush, bushman, hamilton, verstappen can all be hits
-- ge, ie, or me are all valid hits if found inside the last_name
WHERE last_name REGEXP '[gim]e'

-- represents a range therefore ae, be, ce, de, become, acer are all valid hits if found inside the last_name
WHERE last_name REGEXP '[a-d]e'


-- REGEXP Recap
-- ^  beginning 
-- $ ending
-- | logical or
-- [abcd] list
-- [a-d] range


-- the NULL operator
WHERE phone is NULL 

-- the NOT NULL syntax
WHERE phone is NOT NULL

-- the ORDER BY clause in descending format using DESC clause
-- Note: You can order by any column regardless of it being in the SELECT clause or not or even by an alias
ORDER BY state DESC, first_name 

-- order of clauses
USE
SELECT 
FROM
WHERE
ORDER BY
LIMIT  

-- order of logical operators
()
AND
OR
-- AS is used to assign specific names to columns
SELECT quantity * unit_price AS total_price

-- the LIMIT clause
WHERE points < 3000
LIMIT 4

-- 6 represents an offset - skip 6 show next 3 ids 7, 8, 9
WHERE points < 3000
LIMIT 6,3

-- The JOIN clause - Used to combine records column-wise
-- inner joins links columns in different tables
-- the ON phrase gives the condition for the join
-- by default join is inner joined
SELECT o.order_id, o.customer_id, c.first_name, c.last_name 
FROM orders o -- o is the abbreviation
JOIN customers c
	ON o.customer_id = c.customer_id

-- joining across databases
SELECT *
FROM sql_store.order_items o
JOIN sql_inventory.products p
	ON o.product_id = p.product_id

-- self join
USE sql_hr;
SELECT e.employee_id, e.first_name AS employees, m.first_name AS manager
FROM employees e
JOIN employees m
	ON e.reports_to = m.employee_id

-- joining multiple tables
SELECT o.order_id, o.order_date, c.first_name, c.last_name, os.name
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
JOIN order_statuses os
	ON o.status = os.order_status_id
ORDER BY order_date

-- compound join conditions to uniquely join tables where a column has duplicated values hence cannot be used alone
SELECT * 
FROM order_items oi
JOIN order_item_notes oin
	ON oi.order_Id = oin.order_Id
    AND oi.product_id = oin.product_id

-- implicit join syntax
SELECT * 
FROM orders o, customers c
WHERE o.customer_id = c.customer_id

-- outer joins
-- They are outer and inner joins.
-- the left join returns everything from the left table ie the customers table despite the condition of the join so we should have some null values where the condition is not met
 -- so the code below states that return all the customers including those that didn't have any orders placed
SELECT *
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id

-- the right join return the right table despite the condition ie. select everything from customers table despite if they placed an order or not - same as above since we alternated the from tables and now only the order on row axis will be different
SELECT *
FROM orders o
RIGHT JOIN customers c
    ON c.customer_id = o.customer_id

-- the code below states that return all orders which is an inner join since all orders have to be placed by somebody - no null orders
SELECT *
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id

-- outer join between multiple tables
SELECT o.order_date, o.order_id, c.first_name, sh.name, os.name
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
LEFT JOIN shippers sh
	ON o.shipper_id = sh.shipper_id
JOIN order_statuses os
	ON o.status = os.order_status_id
ORDER BY status

-- self outer joins
USE sql_hr;
SELECT e.employee_id, e.first_name AS employees, m.first_name AS manager
FROM employees e
LEFT JOIN employees m
	ON e.reports_to = m.employee_id

-- the USING clause
-- simplifyies the ON phrase if both tables to join have same column name
FROM orders o
JOIN customers c
	USING(customer_id)
LEFT JOIN shippers sh
	USING (shipper_id)
JOIN order_statuses os
	ON o.status = os.order_status_id
ORDER BY status


FROM order_items oi
JOIN order_item_notes oin
	USING (order_Id, product_id) -- for join statement which require atleast 2 columns to get a unique record

-- NATURAL join gives the database engine access to make join conditions on its own
SELECT *
FROM orders o
NATURAL JOIN customers c

-- CROSS joins: join every record in first table to every record in the second table
-- useful when joining a product to different sizes or quantities
-- explicit syntax
SELECT c.first_name AS customer, p.name AS product
FROM products p
CROSS JOIN customers c
ORDER BY c.first_name
-- implicit syntax
SELECT c.first_name AS customer, p.name AS product
FROM products p, customers c
ORDER BY c.first_name

-- UNION - to combine the records for multiple queries row-wise against same or different tables
-- make sure the no of columns returned from both tables are the same
SELECT customer_id, first_name, points, 'Gold' AS type -- Note how we create a new column implicitly and assign it the value of 'Gold
FROM customers
WHERE points > 3000
UNION
SELECT customer_id, first_name, points, 'Silver' AS type
FROM customers
WHERE points BETWEEN 2000 AND 3000
UNION
SELECT customer_id, first_name, points, 'Bronze' AS type
FROM customers
WHERE points < 2000
ORDER BY points DESC

-- let's get all people involved in this trade
SELECT first_name FROM customers
UNION
SELECT name FROM shippers

-- inserting into a single row
-- use the column attributes table to check the syntax
-- datatypes include: INT, VARCHAR, CHAR, DATE
INSERT INTO customers
VALUES (DEFAULT,
            'Bushie',
            'man',
            '2000-01-01',
            NULL,
            NULL,
            'Nairobi',
            NULL,
            DEFAULT
            )
-- if the first and last name are not specified in insert into line then all default and null values in the table have to be declared like above
-- each record should have either a assigned, default or null value
INSERT INTO customers (first_name, last_name)
VALUES ('Bush', 'Man')

-- inserting multiply rows
INSERT INTO shippers (name)
VALUES ('Shipper1'),
       ('Shipper2'),
       ('Shipper3')

-- inserting hierarchical rows: insert into multiple tables
INSERT INTO orders (customer_id, order_date, status) 
VALUES (1, '1990-01-01', 1) -- the order_id will be generated automatically which we can then use in our order_items table since both values should be the same ie order_id

INSERT INTO order_items
VALUES (LAST_INSERT_ID(), 1, 1, 3.45), -- LAST_INSERT_ID func returns the last AI value 
       (LAST_INSERT_ID(), 2, 1, 5.45)

-- creating a new TABLE 
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT, -- other int attributes include: tinyint(), smallint()
    email VARCHAR(255) NOT NULL UNIQUE, 
    bio TEXT,
    country VARCHAR(2)
)ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; -- you can google this out

CREATE TABLE roome(
    id INT AUTO_INCREMENT, 
    street VARCHAR(255),
    owner_id INT NOT NULL, 
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id) REFERENCES users(id)
)

-- creating indexes
CREATE INDEX email_index ON users(email);

-- creating a copy of a table
CREATE TABLE orders_archive AS -- the PK and AI attributes are ignored in the new table 
SELECT * FROM orders

-- creating a table using a subquery
CREATE TABLE invoices_archived AS 
SELECT i.invoice_id, i.number, c.name, i.invoice_total, i.payment_total
FROM invoices i
JOIN clients c
	USING(client_id)
WHERE i.payment_date IS NOT NULL

-- updating a single row
UPDATE invoices
SET payment_total = 10, payment_date = '1990-10-01'
WHERE invoice_id = 1

-- updating multiple rows
-- use a general condition
UPDATE invoices
SET payment_total = 10, payment_date = '1990-10-01'
WHERE client_id = 3

UPDATE invoices
SET payment_total = payment_total*1.5, payment_date = '1990-10-01' -- update by modifying existing columns
WHERE client_id = 3

-- using subqueries in updates
UPDATE invoices
SET payment_total = 10, payment_date = '1990-10-01'
WHERE client_id = (
            SELECT client_id
            FROM clients
            WHERE name = 'MyWorks'
) -- the code inside parenthesis returns the client_id which we can then use to update our invoices table

-- for multiple subquery results 
UPDATE invoices
SET payment_total = 10, payment_date = '1990-10-01'
WHERE client_id IN 
            (SELECT client_id
            FROM clients
            WHERE state IN ('NY', 'CA')) -- returns 2 values thus we use IN instead of =

UPDATE orders
SET comments = 'Gold Customers'
WHERE customer_id IN
            (SELECT customer_id
            FROM  customers c
            WHERE points > 3000)

-- deleting rows
DELETE FROM invoices
WHERE invoice_id = 2

-- using subqueries
DELETE FROM invoices
WHERE client_id IN (
            SELECT client_id
            FROM clients
            WHERE name = 'MyWorks'
)

-- DATABASES
-- Creating DBS
DROP DATABASE IF EXISTS `sql_hr`; -- First drop DB if it exists as a cautionary measure
CREATE DATABASE `sql_hr`; --creating the DB
USE `sql_hr`; -- activating the DB
