import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px
from PIL import Image


def app():
    dataset = st.container()

    with dataset:
        st.title("TPE-48 Keywords Data")
        df = pd.read_excel('./Data/KwsData/TPE48.xlsx')
        #st.dataframe(df)

    # filter by search volume
    min_sv = min(df['Search Volume'])
    max_sv = max(df['Search Volume'])
    sv_selection = (min_sv, max_sv)
    sv = df['Search Volume'].unique().tolist()

    # 4.1 data selection
    sv_selection = st.slider('Search Volume',
                             min_sv,
                             max_sv,
                             value=(min_sv, max_sv),
                             step=10)
    mask_1 = df['Search Volume'].between(*sv_selection)
    number_of_results = df[mask_1].shape[0]
    st.markdown(f'Availabel Results: {number_of_results}')

    # data dispaly
    df_grouped_1 = df[mask_1]
    st.dataframe(df_grouped_1)
    scatter = px.scatter(df_grouped_1,
                         x='Search Volume',
                         y='Competing',
                         size='CPR',
                         color='Ave. Price',
                         hover_name='Phrase',
                         )
    st.plotly_chart(scatter)





