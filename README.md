# dob-jobs-parser
NYC Department of Building's job data -> postgres

Builds a database of DOB data. Also see: https://github.com/aepyornis/DOB-Jobs

Download the data: 

```
wget https://data.cityofnewyork.us/api/views/ic3t-wcy2/rows.csv?accessType=DOWNLOAD -O job_fillings.csv
```

Create a psql database: ``` createdb dobjobs ```

Create a file *env.sh* with two bash functions with your PG connection parameters:

``` bash
export PGPASSWORD=PASSWORD

alias _psql="psql -h HOST -d DATABASE -U USER"

execute_sql () {
    _psql -f "$1"
}

execute_sql_cmd () {
    _psql --command "$1"
}

```

Create python3 virtual evnironment & install dependencies: ``` make ```

Import the data: ``` ./venv/bin/dobjobs  --psql -H <HOST> -U <USER> -P <PASSWORD> -D <DATABASE> /path/to/job_fillings.csv ```

If you have the table 'pluto_16v2', add lat & lng to dobjobs. Otherwise skip this step:

```
execute_sql  sql/geocode.sql
```

Add computed columns and index:

``` 
execute_sql sql/add_columns.sql
execute_sql sql/index.sql
```
