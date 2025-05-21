"""A simple Streamlit dashboard."""

from os import environ as ENV

from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import altair as alt

from data import load_rabbit_dataset, filter_rabbits, get_boto3_session, get_academic_levels_count
from charts import get_behaviour_bar_chart

if __name__ == "__main__":

    load_dotenv()

    aws_session = get_boto3_session(access_key=ENV["AWS_ACCESS_KEY"], secret_key=ENV["AWS_SECRET_ACCESS_KEY"])
    rabbits = load_rabbit_dataset(ENV["RABBIT_CSV_URL"])
    levels = get_academic_levels_count(ENV["ATHENA_DB_NAME"], aws_session)

    unique_rabbit_count = rabbits["rabbit"].nunique()

    st.title("Rabbits")
    st.metric("Number of rabbits", unique_rabbit_count, delta=2)

    relevant_rabbits = st.sidebar.multiselect("Relevant Rabbits",
                                      options=rabbits["rabbit"].unique(),
                                      default=rabbits["rabbit"].unique())
    sorted = st.sidebar.checkbox("Sorted", value=False)
    
    rabbits = filter_rabbits(rabbits, relevant_rabbits)

    left, right = st.columns(2)

    with left:
        st.subheader("Good rabbits")
        st.altair_chart(get_behaviour_bar_chart(rabbits, "good", sorted))
    
    with right:
        st.subheader("Bad rabbits")
        st.altair_chart(get_behaviour_bar_chart(rabbits, "bad", sorted))
    print("Charts generated!")