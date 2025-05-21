import pandas as pd
import altair as alt
import streamlit as st

@st.cache_data(ttl=3)
def get_behaviour_bar_chart(data: pd.DataFrame, behaviour_type: str, sorted: bool=False) -> alt.Chart:
    """Returns a bar chart of behaviour counts."""
    behaviour = data[data["behavior"] == behaviour_type]
    behaviour_counts = behaviour["rabbit"].value_counts().reset_index()
    return alt.Chart(behaviour_counts).mark_bar().encode(
        x=alt.X("rabbit", sort="y") if sorted else "rabbit",
        y="count")
