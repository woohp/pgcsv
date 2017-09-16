# pgcsv

pgcsv executes PostgreSQL sql queries and output the results in a csv format.
It accepts sql queries via stdin and outputs to stdout.
It is recommended that you validate the correctness of your query elsewhere, perhaps in psql, before running pgcsv.

## Usage
```bash
# basic example
pgcsv -h <dbhost> -p <dbport> < my_commands.sql > results.csv

# you can compress your output using a pipe
pgcsv -h <dbhost> -p <dbport> < my_commands.sql | gzip - > results.csv.gz
```
