-- the USE clause selects the database to use
USE sql_store
-- the SELECT clause selects every column from customers table
-- the FROM  clause references the target table
SELECT * 
FROM customers

-- selects specific columns from customers table
SELECT customers_id, first_name
FROM customers


-- the WHERE  clause filters data
SELECT *
FROM customers
WHERE points > 3000

-- comparison operators
>, <, >=, <=, !=, <>, =

-- AND operator has a higher precedence than OR operator but can be overwritten by using parenthesis

-- the AND, OR operators
WHERE (birth_date > '1990-01-01' OR points > 1000) AND state = 'VA'

-- the NOT operator
WHERE NOT(birth_date > '1990-01-01' OR points > 1000)

-- the IN operator
WHERE state IN ('VA', 'NY', 'LA')

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

-- the % represents a b somewhere inside the last_name
WHERE last_name LIKE '%b%'

-- the % represents any number of characters before b
WHERE last_name LIKE '%b'

-- each underscore represents a character therefore the word is a three digit word ending with b
WHERE last_name LIKE '__b'

-- the REGEXP operator shows b is anywhere in the word
WHERE last_name REGEXP 'b'

-- the caret shows b is at the beginning of the word
WHERE last_name REGEXP '^b'

-- the caret shows b is at the end of the word
WHERE last_name REGEXP 'b$'

-- the pipe represents multiple search patterns 
WHERE last_name REGEXP 'bush|vera'

-- ge, ie, or me are all valid hits if found inside the last_name
WHERE last_name REGEXP '[gim]e'

-- represents a range therefore ae, be, ce, or de are all valid hits if found inside the last_name
WHERE last_name REGEXP '[a-d]e'

-- the NULL operator
WHERE phone is NULL 

-- the NOT NULL syntax
WHERE phone is NOT NULL

-- the ORDER BY clause
ORDER BY first_name, last_name DESC 

-- order of clauses
USE
SELECT 
FROM
WHERE
ORDER BY
LIMIT  

-- AS is used to assign specific names to columns
SELECT quantity * unit_price AS total_price

-- the LIMIT clause
WHERE points < 3000
LIMIT 4

-- 6 represents an offset - skip 6 show id 7, 8, 9
WHERE points < 3000
LIMIT 6,3

-- inner joins links columns in different tables
-- the ON phrase gives the condition for the join
-- by default join is inner joined
SELECT o.order_id, o.customer_id, c.first_name, c.last_name 
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id

-- joining across databases
USE sql_store;
SELECT *
FROM order_items o
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

-- compound join conditions
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
-- the left join returns everything from the customers table despite the condition of the join
-- by default join is right joined
SELECT *
FROM customers c
LEFT JOIN orders o
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
-- simplifyies the ON phrase
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
	USING (order_Id, product_id)

-- NATURAL join gives the database engine access to make join conditions on its own
SELECT *
FROM orders o
NATURAL JOIN customers c

-- CROSS joins
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

-- UNION
SELECT customer_id, first_name, points, 'Gold' AS type
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
ORDER BY first_name

-- inserting into a single row
-- use the column attributes table to check the syntax
-- if the first and last name are not specified in insert into line then all default and null values in the table have to be declared
INSERT INTO customers (first_name, last_name)
VALUES ('Bush', 'Man')

-- inserting multiply rows
INSERT INTO shippers (name)
VALUES ('Shipper1'),
       ('Shipper1'),
       ('Shipper1')

-- inserting hierarchical rows
INSERT INTO orders (customer_id, order_date, status)
VALUES (1, '1990-01-01', 1)

INSERT INTO order_items
VALUES (LAST_INSERT_ID(), 1, 1, 3.45),
       (LAST_INSERT_ID(), 2, 1, 5.45)

-- creating a new TABLE 
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE, 
    bio TEXT,
    country VARCHAR(2)
)

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
CREATE TABLE orders_archive AS 
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

-- using subqueries in updates
UPDATE invoices
SET payment_total = 10, payment_date = '1990-10-01'
WHERE client_id = (
            SELECT client_id
            FROM clients
            WHERE name = 'MyWorks'
)
-- for multiple subquery results 
UPDATE invoices
SET payment_total = 10, payment_date = '1990-10-01'
WHERE client_id IN 
            (SELECT client_id
            FROM clients
            WHERE state IN ('NY', 'CA'))

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
WHERE invoice_id IN (
            SELECT client_id
            FROM clients
            WHERE name = 'MyWorks'
)

