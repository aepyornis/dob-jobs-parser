# dob-jobs-parser
NYC Department of Building's job data -> postgres

Builds a database of DOB data. Also see: https://github.com/aepyornis/DOB-Jobs

download the data: 

```
wget https://data.cityofnewyork.us/api/views/ic3t-wcy2/rows.csv?accessType=DOWNLOAD -O job_fillings.csv
```

create a database: ``` createdb dobjobs ```

Set connection settings env variable for the parser: 

``` export DOBJOBS_CONNECTION='connection string' ```
sample string: "dbname=dobjobs user=ziggy"

create python3 virtual evnironment & install dependencies:
```
pyvenv venv
source venv/bin/activate
pip install psycopg2
```

run the parser: ``` python3 csvparser/db_dobjobs.py /path/to/jobs_fillings.csv ```

add lat/lng to database
(you have to update sql/geocode.sql with the correct path to the bbl, lat, lng lookup file.)

```
cd ..
psql -d dobjobs -f sql/geocode.sql
```

add columns:

``` 
psql -d dobjobs -f sql/add_columns.sql
```

Add indexes, which requires pg_trgm extension. You can install this module with the postgresql-contrib package:

``` sudo apt-get install postgresql-contrib  ```

```
psql -d dobjobs -f sql/index.sql
```
