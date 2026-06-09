import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="MLS Player Similarity Dashboard",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ MLS Player Similarity Dashboard")
st.markdown("### Who Plays Like Lionel Messi?")

@st.cache_data
def load_data():
    url = "url = "https://raw.githubusercontent.com/JHastings46/Soccer-Similarity-Model-/main/messi_scout_output_combined%20(3).csv"
    df = pd.read_csv(url)
    df.columns = df.columns.str.lower().str.strip()
    return df

df = load_data()

st.sidebar.header("Filters")

role_options = ["All"] + sorted(df["target_role"].dropna().unique().tolist())
selected_role = st.sidebar.selectbox("Target Role", role_options)

fit_options = ["All"] + sorted(df["fit_bucket"].dropna().unique().tolist())
selected_fit = st.sidebar.selectbox("Fit Bucket", fit_options)

uncertainty_options = ["All"] + sorted(df["uncertainty_band"].dropna().unique().tolist())
selected_uncertainty = st.sidebar.selectbox("Uncertainty Band", uncertainty_options)

min_similarity = st.sidebar.slider(
    "Minimum Similarity Score",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.05
)

top_n = st.sidebar.slider(
    "Top N Players",
    min_value=5,
    max_value=50,
    value=15,
    step=5
)

filtered = df.copy()

if selected_role != "All":
    filtered = filtered[filtered["target_role"] == selected_role]

if selected_fit != "All":
    filtered = filtered[filtered["fit_bucket"] == selected_fit]

if selected_uncertainty != "All":
    filtered = filtered[filtered["uncertainty_band"] == selected_uncertainty]

filtered = filtered[filtered["similarity_score"] >= min_similarity]
filtered = filtered.sort_values("similarity_score", ascending=False).head(top_n)

col1, col2, col3 = st.columns(3)
col1.metric("Players Shown", len(filtered))
col2.metric("Avg Similarity Score", round(filtered["similarity_score"].mean(), 3) if len(filtered) > 0 else 0)
col3.metric("Top Match", filtered["player"].iloc[0] if len(filtered) > 0 else "None")

st.markdown("---")

display_cols = [
    "player", "team", "competition", "season", "target_role",
    "age", "minutes", "goals_per90_adj", "shots_per90_adj",
    "similarity_score", "uncertainty_band", "fit_bucket", "summary"
]

available_cols = [col for col in display_cols if col in filtered.columns]

def color_fit_bucket(val):
    if val == "younger alternative":
        return "background-color: #c8e6c9"
    elif val == "upside bet":
        return "background-color: #fff9c4"
    else:
        return "background-color: #ffccbc"

def color_uncertainty(val):
    if val == "Low":
        return "color: green; font-weight: bold"
    elif val == "Medium":
        return "color: orange; font-weight: bold"
    else:
        return "color: red; font-weight: bold"

styled = filtered[available_cols].style\
    .applymap(color_fit_bucket, subset=["fit_bucket"])\
    .applymap(color_uncertainty, subset=["uncertainty_band"])\
    .format({"similarity_score": "{:.3f}", "goals_per90_adj": "{:.2f}", "shots_per90_adj": "{:.2f}"})\
    .hide(axis="index")

st.dataframe(filtered[available_cols].reset_index(drop=True), use_container_width=True)

st.markdown("---")
st.markdown("**Dashboard built by Joel Hastings | Data: FBref MLS | Model: Bayesian-adjusted cosine similarity**")
