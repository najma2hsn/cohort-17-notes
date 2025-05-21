"""A small example of using AWS Wrangler."""

from os import environ as ENV

from boto3 import Session
from dotenv import load_dotenv
import awswrangler as wr

if __name__ == "__main__":

    load_dotenv()

    aws_session = Session(aws_access_key_id=ENV["AWS_ACCESS_KEY"],
                          aws_secret_access_key=ENV["AWS_SECRET_ACCESS_KEY"],
                          region_name="eu-west-2")
    
    print(wr.s3.list_buckets(boto3_session=aws_session))

    print(wr.athena.read_sql_query(sql="SELECT COUNT(truck_name) AS truck_count FROM truck;",
                                   database=ENV["ATHENA_DB_NAME"],
                                   boto3_session=aws_session))
    