"""A simple Streamlit dashboard."""

from os import environ as ENV

from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import altair as alt

if __name__ == "__main__":

    load_dotenv()

    rabbits = pd.read_csv(ENV["RABBIT_CSV_URL"])

    print(rabbits.head())