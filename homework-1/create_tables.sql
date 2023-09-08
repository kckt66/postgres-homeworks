-- SQL-команды для создания таблиц
CREATE TABLE customers_data
(
	customer_id varchar(100) PRIMARY KEY,
	company_name text,
	contact_name text
);


CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE orders_data
(
	order_id int,
	customer_id varchar(100) REFERENCES customers_data(customer_id) NOT NULL,
	employee_id int REFERENCES employees_data(employee_id) NOT NULL,
	order_date date NOT NULL DEFAULT CURRENT_DATE,
	ship_city varchar(100)
);
