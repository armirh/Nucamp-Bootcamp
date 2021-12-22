-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;
-- connect via psql
\c week1_workshop

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY(id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);

-- TASK 1: create table suppliers
CREATE TABLE suppliers (
    id SERIAL,
    name TEXT NOT NULL,
    PRIMARY KEY(id)
);

-- TASK 2: create a customers table
CREATE TABLE customers (
    id SERIAL,
    name TEXT NOT NULL,
    PRIMARY KEY(id)
);

-- TASK 3: create an employees table
CREATE TABLE employees (
    id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY(id)
);
-- TODO create more tables here...

-- TASK 4: create an orders table
CREATE TABLE orders (
    id SERIAL,
    order_date date,
    employee_id INT,
    customers_id INT,
    PRIMARY KEY(id)
);

-- TASK 5:
CREATE TABLE order_products (
    order_id INT,
    product_id INT,
    PRIMARY KEY(order_id, product_id)
);

-- TASK 6:
CREATE TABLE territories (
    id SERIAL,
    description TEXT NOT NULL,
    PRIMARY KEY(id)
);

-- TASK 7:
CREATE TABLE employees_territories (
    employee_id INT,
    territories_id INT,
    PRIMARY KEY(employee_id,territories_id)
);

-- TASK 8:
CREATE TABLE offices (
    id SERIAL,
    address_line TEXT NOT NULL,
    territories_id INT,
    PRIMARY KEY(id)
);

-- TASK 9:
CREATE TABLE us_states (
    id SERIAL,
    state_name TEXT NOT NULL UNIQUE,
    state_abbrv varchar(2) NOT NULL,
    PRIMARY KEY(id)
);

---
--- Add foreign key constraints
---

ALTER TABLE products
ADD CONSTRAINT fk_products_categories 
FOREIGN KEY (category_id) 
REFERENCES categories;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_costumer
FOREIGN KEY (customers_id)
REFERENCES customers;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_employee
FOREIGN KEY (employee_id)
REFERENCES employees;

ALTER TABLE order_products
ADD CONSTRAINT fk_order_products_order
FOREIGN KEY (order_id)
REFERENCES orders;

ALTER TABLE order_products
ADD CONSTRAINT fk_order_products_product
FOREIGN KEY (product_id)
REFERENCES products;

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_employee
FOREIGN KEY (employee_id)
REFERENCES employees;

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_territories
FOREIGN KEY (territories_id)
REFERENCES territories;

ALTER TABLE offices
ADD CONSTRAINT fk_offices_territories
FOREIGN KEY (territories_id)
REFERENCES territories;

-- TODO create more constraints here...

-- TASK 10:
ALTER TABLE orders ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customers_id) REFERENCES customers;

ALTER TABLE orders ADD CONSTRAINT fk_orders_employees
FOREIGN KEY (employee_id) REFERENCES employees;

-- TASK 11:
ALTER TABLE products ADD CONSTRAINT fk_products_suppliers
FOREIGN KEY (supplier_id) REFERENCES suppliers;

-- TASK 12:
ALTER TABLE order_products ADD CONSTRAINT fk_orders_products_products
FOREIGN KEY (product_id) REFERENCES products;

ALTER TABLE order_products ADD CONSTRAINT fk_orders_products_orders
FOREIGN KEY (order_id) REFERENCES orders;

-- Task 13: Employees-Territories
ALTER TABLE employees_territories ADD CONSTRAINT fk_employees_territories_territories
FOREIGN KEY (territory_id) REFERENCES territories;

ALTER TABLE employees_territories ADD CONSTRAINT fk_employees_territories_employees
FOREIGN KEY (employee_id) REFERENCES employees;

-- Task 14: Offices
ALTER TABLE offices ADD CONSTRAINT fk_offices_territories
FOREIGN KEY (territory_id) REFERENCES territories;