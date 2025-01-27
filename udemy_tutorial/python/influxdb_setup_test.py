import random

import influxdb_client
import os
import time
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = "influxdb url"
token = "influxdb token"
org = "Org name"
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
print(f"Ping Response: {client.ping()}")
source_bucket = "test_bucket"
team = "EQUIP"

query_api = client.query_api()
query = f"""from(bucket: "test_bucket")
         |> range(start: -24h)
         |> filter(fn: (r) => r._measurement == "EQUIP" and r.workflow == "assethub" and r.track == "staging" and r.api == "GetInteractionDataQuery" and r.user_count|spawn_rate == "u=10|r=5" and r.baseline_test == "true")
         |> filter(fn: (r) => r._field == "tp75")
         |> drop(columns: ["_start", "_stop", "_time", "failure_count"])"""
tables = query_api.query(query, org=org)
print(f'tables: {tables}')

for table in tables:
    for record in table.records:
        print(record)
