# 1. import
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image


# 2. load dataframe
header = st.container()
dataset = st.container()

with header:
    st.title("Welcome to my data web")
    st.text("in this project, i will try some data visulization")

with dataset:
    st.title("this is dataset section")
    df = pd.read_excel('./TPE30.xlsx')
    st.dataframe(df)

# 3. filter, group dataframe
# filter by search volume
min_sv = min(df['Search Volume'])
max_sv = max(df['Search Volume'])
sv_selection = (min_sv, max_sv)
sv = df['Search Volume'].unique().tolist()





# 4. plot data
# 4.1 data selection
sv_selection = st.slider('Search Volume',
                         min_sv,
                         max_sv,
                         value=(min_sv,max_sv),
                         step=10)
mask_1 = df['Search Volume'].between(*sv_selection)
number_of_results = df[mask_1].shape[0]
st.markdown(f'Availabel Results: {number_of_results}')


# 4.2 data dispaly
df_grouped_1 = df[mask_1]
df_grouped_1
scatter = px.scatter(df_grouped_1,
                     x='Search Volume',
                     y='Competing',
                     size='CPR',
                     color='CPR',
                     hover_name='Phrase',
                     )
scatter


