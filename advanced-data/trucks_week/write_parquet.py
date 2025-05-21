from glob import glob

from boto3 import client
import pyarrow as pa
import pandas as pd

def load_to_s3(s3_client: client, data: pd.DataFrame, filepath: str):
    table = pa.Table.from_pandas(data)
    pq_buffer = pa.BufferOutputStream()
    pq.write_table(table, pq_buffer)
    s3_client.put_object(
            Body=bytes(pq_buffer.getvalue()),
            Bucket=ENV["TARGET_BUCKET_NAME"],
            Key=filepath,
        )
    
def get_file_paths():
    return glob("./truck/*/*/*/transaction.parquet")

for file in get_file_paths():
    print(file)


# {
#     2025: {
#         10: {
#             5: {
#                 pd.DataFrame("Data")
#             }
#         }
#     }
# }