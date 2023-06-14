import pandas as pd
import json
import time

# Function to convert JSON to CSV
def json_to_csv(json_file, csv_file):
    with open(json_file) as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)
    df.to_csv(csv_file, index=False)

# Function to convert JSON to SQL
def json_to_sql(json_file, sql_file):
    with open(json_file) as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)
    df.to_sql('table_name', 'sqlite:///' + sql_file, if_exists='replace')

# Specify the paths for JSON, CSV, and SQL files
json_file = '0.json'
csv_file = 'output.csv'
sql_file = 'output.db'

# Convert JSON to CSV and measure the time taken
start_time = time.time()
json_to_csv(json_file, csv_file)
csv_time = time.time() - start_time

# Convert JSON to SQL and measure the time taken
start_time = time.time()
json_to_sql(json_file, sql_file)
sql_time = time.time() - start_time

# Print the time taken for conversion
print(f"Time taken to convert JSON to CSV: {csv_time} seconds")
print(f"Time taken to convert JSON to SQL: {sql_time} seconds")
