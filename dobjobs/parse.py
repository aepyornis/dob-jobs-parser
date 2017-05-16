import csv
import datetime
import os
import sys
import argparse
import dobjobs.bbl as bbl
import dobjobs.db as db

# => tuple
def headers():
    """ returns tuple of headers """
    with open(os.path.dirname(__file__) + '/headers.txt', 'r') as f:
        return tuple([x for x in f.read().split('\n') if len(x) > 1])

def headers_with_bbl():
    """ headers  plus the columns bbl """
    return headers() + ('bbl',)


def type_lookup():
    """ Reads the sql schema and returns a map of fields names to types.
    The layout and capitalization of schema.sql, which doesn't matter for the
    database, does impact this function.
    """
    d = {}
    with open(os.path.dirname(__file__) + '/schema.sql', 'r') as f:
        for line in f:
            if ')' not in line or 'char' in line:
                key = line.strip().replace(',', '').split(' ')[0]
                val = ' '.join(line.strip().replace(',', '').split(' ')[1:])
                d[key] = val
    return d


def date_format(datestring):
    """ mm/dd/yyyy string -> datetime date object """
    datelist = datestring[0:10].split('/')
    datelist = [int(x) for x in datelist]
    datetuple = (datelist[2], datelist[0], datelist[1])
    return datetime.date(*datetuple)


# str, str, dict -> None|Boolean|str|int|datetime.date or throws
def type_cast_field(column, value, lookup):
    datatype = lookup[column].strip()
    if datatype == 'boolean':
        return bool(value.strip())
    elif value.strip() == '':
        return None
    elif datatype == 'text' or 'char' in datatype:
        return value.strip()
    elif datatype == 'integer':
        try:
            return int(value.strip())
        except ValueError:
            return None
    elif datatype == 'money':
        return value.strip().replace('$', '')
    elif datatype == 'date':
        try:
            return date_format(value.strip())
        except ValueError:
            return None
    else:
        raise Exception('Type Cast Error - ' + datatype)


# Dict -> Dict
def type_cast_row(dict_row, lookup):
    """ turns strings into python data types, fixes common problems """
    d = {}
    for key in dict_row:
        d[key] = type_cast_field(key, dict_row[key], lookup)
    return d


# str -> generator
def read_csv(csv_path):
    """ reads csv, parses fields, returns generator of dictionaries """
    columns = headers()
    lookup = type_lookup()
    with open(csv_path, 'r') as f:
        next(f) # skip header row
        csv_reader = csv.reader(f)
        for line in csv_reader:
            yield type_cast_row(dict(zip(columns, line)), lookup)

# generator => g            
def add_bbl(csv_generator):
    """ adds bbl field to dict """
    for row in csv_generator:
        row.update({'bbl': bbl.bbl(row['Borough'], row['Block'], row['Lot'])})
        yield row


def write_csv(infile, outfile):
    """ writes csv to outfile """
    csv_writer = csv.DictWriter(outfile, headers_with_bbl())
    for row in add_bbl(read_csv(infile)):
        csv_writer.writerow(row)


def to_db(infile, **kwargs):
    """ copys to db """
    tmp_file = '__tmp.csv'
    # save csv to tmp file
    with open(tmp_file, 'w') as f:
        write_csv(infile, f)

    conn = db.connection(**kwargs)
    db.create_table(conn)
    cur = conn.cursor()
    cols = headers_with_bbl()

    # use postgres COPY to copy tmp csv to database
    with open(tmp_file, 'r') as f:
        cur.copy_expert(db.copy_string(cols), f)

    conn.commit()
    conn.close()
    os.remove(tmp_file)


def main():
    parser = argparse.ArgumentParser(description='clean and parse department of buildings jobs. Writes cleaned csv to stdout unless option --psql is invoked.')
    parser.add_argument('file', help='path to job filings csv')
    parser.add_argument("--psql", help="Insert data into postgres", action="store_true")
    parser.add_argument("-U", "--user", help="Postgres user. default: postgres", default="postgres")
    parser.add_argument("-P", "--password", help="Postgres password. default: postgres", default="postgres")
    parser.add_argument("-H", "--host", help="Postgres host: default: 127.0.0.1", default="127.0.0.1")
    parser.add_argument("-D", "--database", help="postgres database: default: postgres", default="postgres")
    args = parser.parse_args()
    if args.psql:
        to_db(args.file, user=args.user, password=args.password, host=args.host, database=args.database)
    else:
        write_csv(args.file, sys.stdout)

if __name__ == '__main__':
    main()
