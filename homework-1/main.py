"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import pathlib
from pathlib import Path


work_path = pathlib.Path.cwd()

customers = Path(work_path, 'customers_data.csv')
employee = Path(work_path, 'employees_data.csv')
orders = Path(work_path, 'orders_data.csv')

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='Zrjdktd13rjycnfynby55')


try:
    with conn:
        with conn.cursor() as cur:

            with open(customers, encoding='utf-8') as file:
                data = csv.DictReader(file, delimiter=',')
                for i in data:
                    cur.execute("INSERT INTO customers_data VALUES (%s, %s, %s)", (i['customer_id'], i['company_name'], i['contact_name']))
            
   
            with open(employee, encoding='utf-8') as file:
                data = csv.DictReader(file, delimiter=',')
                for i in data:
                    cur.execute("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)", (i['employee_id'], i['first_name'],\
                    i['last_name'], i['title'], i['birth_date'], i['notes']))
                    
            
            with open(orders, encoding='utf-8') as file:
                data = csv.DictReader(file, delimiter=',')
                for i in data:
                    cur.execute("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)", (i['order_id'], i['customer_id'], i['employee_id'],\
                    i['order_date'], i['ship_city']))

finally:
    conn.close()

        



