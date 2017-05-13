import os
import psycopg2

def create_table(conn):
    """ drops and recreates dobjobs """
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS dobjobs')
    with open(os.path.dirname(__file__) + '/schema.sql', 'r') as f:
        sql = f.read()
        cur.execute(sql)
    conn.commit()

def connection(**kwargs):
    return psycopg2.connect(**kwargs)

def copy_string(cols):
    column_list = ','.join(cols)
    return "COPY dobjobs ({column_list}) FROM STDIN WITH (FORMAT csv, HEADER FALSE, NULL '')".format(column_list=column_list)
