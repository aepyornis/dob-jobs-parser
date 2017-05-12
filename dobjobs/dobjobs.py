"""
python3

Inserts dob application files csv data (from nyc open) into postgres
"""
import csv
import datetime
import os
import sys
from dobjobs import util
import psycopg2

def create_table(cur):
    cur.execute('DROP TABLE IF EXISTS dobjobs')
    with open(os.path.dirname(__file__) + '/schema.sql', 'r') as f:
        sql = f.read()
        cur.execute(sql)


def get_headers():
    with open('headers.txt', 'r') as f:
        return f.read().replace('\n', '').split(',')


def insert_row(row, cur, lookup):
    prepared_row = {}
    for key in row:
        try:
            prepared_row[key] = util.type_cast(key, row[key], lookup)
        except ValueError as e:
            # print(key + "," + row[key])
            # print(e)
            global errors
            errors += 1
            prepared_row[key] = None

    query = util.make_query('dobjobs', prepared_row)[0]
    data = util.make_query('dobjobs', prepared_row)[1]
    cur.execute(query, data)


def copy_data(csv_path, cur, lookup):
    global errors
    with open(csv_path, 'r') as f:
        next(f)
        headers = get_headers()
        csvreader = csv.DictReader(f, fieldnames=headers)
        while True:
            try:
                row = next(csvreader).copy()
                row['bbl'] = util.bbl(row['Borough'], row['Block'], row['Lot'])
                insert_row(row, cur, lookup)
            except UnicodeDecodeError:
                errors += 1
            except AttributeError:
                errors += 1
            except StopIteration:
                break

if __name__ == '__main__':
    csv_file = sys.argv[1] # csv_file = 'path/to/DOB_Job_Application_Filings.csv'
    db_connection_string = sys.argv[2]  # os.environ['DOBJOBS_CONNECTION']
    conn = psycopg2.connect(db_connection_string)
    cursor = conn.cursor()
    errors = 0
    lookup = util.sql_type_dir('schema.sql')
    create_table(cursor)
    copy_data(csv_file, cursor, lookup)
    conn.commit()
    print('errors: ' + str(errors))
