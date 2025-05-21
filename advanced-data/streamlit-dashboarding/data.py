import pandas as pd
import streamlit as st
from boto3 import Session
import awswrangler as wr

@st.cache_data
def load_rabbit_dataset(url: str) -> pd.DataFrame:
    """Returns a dataframe of rabbit behaviour."""
    print("Loading data...")
    return pd.read_csv(url)


@st.cache_data
def filter_rabbits(df: pd.DataFrame, rabbits: list[str]) -> pd.DataFrame:
    print("Selecting rabbits...")
    return df[df["rabbit"].isin(rabbits)]


@st.cache_resource
def get_boto3_session(access_key: str, secret_key: str):
    """Returns a live Boto3 session."""
    print("Connecting to AWS...")
    aws_session = Session(aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name="eu-west-2")
    return aws_session


@st.cache_data
def get_academic_levels_count(database: str, _session: Session, limit:int=3) -> pd.DataFrame:
    return wr.athena.read_sql_query(sql=f"SELECT academic_level, COUNT(*) as count FROM students GROUP BY academic_level LIMIT :limit_num;",
                                    params = {
                                        "limit_num": limit
                                    },
                                    database=database,
                                    boto3_session=_session)