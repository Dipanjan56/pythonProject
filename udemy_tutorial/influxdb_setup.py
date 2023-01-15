import random

import influxdb_client
import os
import time
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Initialize Client
# os.environ[
#     "INFLUXDB_TOKEN"] = "xwek80n_8hoLa2vK-Vxu_Axi3H0e3FnSMZFcxzEbI82KwsQjTa9n01YqqBHMt7u4iRtMUMThKn194HsQhV-XGQ=="
# token = os.environ.get("INFLUXDB_TOKEN")
# org = "Mindtickle"
# url = "https://us-west-2-1.aws.cloud2.influxdata.com/"
#
# client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
# client = influxdb_client.InfluxDBClient(url="http://localhost:8086", username="dipanjan56", password="Test@123")
url = "http://influxdb2.devops-eks.mindtickle.com"
token = "-ZDWNJKA_bJP2lPfeHmRYBKjU6Klqna8X4YhX6ZesbuKatBo3OHJXCwmji2vH999JxBMFVhQzATrSW4mwwZSww=="
org = "Mindtickle"
# client = influxdb_client.InfluxDBClient(url="http://influxdb2.devops-eks.mindtickle.com",
#                                         token="-ZDWNJKA_bJP2lPfeHmRYBKjU6Klqna8X4YhX6ZesbuKatBo3OHJXCwmji2vH999JxBMFVhQzATrSW4mwwZSww==", org="Mindtickle")
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
print(f"Ping Response: {client.ping()}")
bucket = "test_bucket"
measurement = "measurement"

# writing data: In this query, we define five data points and write each one to InfluxDB. Each of the 5 points we write has a field and a tag.
write_api = client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
    api = f"/v1/api/{value}"
    tp99 = value + random.randrange(10, 1000)
    print(f'api: {api} | tp99: {tp99}')
    point = (
        Point(measurement).tag("track", "prod").tag("api", api).field("tp99", tp99)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    print('writing data')
    time.sleep(1)  # separate points by 1 second

# Fetching data: In this query, we are looking for data points within the last 10 minutes with a measurement of "measurement1".
query_api = client.query_api()

query = f"""from(bucket: "{bucket}")
 |> range(start: -1h)
 |> filter(fn: (r) => r._measurement == "{measurement}")"""
tables = query_api.query(query, org=org)

for table in tables:
    for record in table.records:
        print(record)
#
# # Aggregate Query: In this example, we use the mean() function to calculate the average value of data points in the last 10 minutes.
# query_api = client.query_api()
#
# query = """from(bucket: "Bucket_1")
#   |> range(start: -10m)
#   |> filter(fn: (r) => r._measurement == "measurement1")
#   |> mean()"""
# tables = query_api.query(query, org="Mindtickle")
#
# for table in tables:
#     for record in table.records:
#         print(record)
