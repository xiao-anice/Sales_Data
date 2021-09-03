import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("welcome to my data web")
    st.text("in this project, i will try some data visulization")

with dataset:
    st.title("this is dataset section")
    st.text("um....")
    df = pd.read_excel('./test.xlsx')
    st.write(df.head(100))
    st.subheader("Search Volume")
    st.bar_chart(df['Search Volume'])
    st.subheader("Competing")
    st.bar_chart(df['Competing'])


with features:
    st.title("this is feature section")


with model_training:
    st.title("this is model training session")
    sel_col, disp_col = st.columns(2)
    max_depth = sel_col.slider("what?",min_value=100, max_value=100000, value=100, step=10)
    n_estimators = sel_col.selectbox("select?", options=[100, 200, 300, 'no limit'], index=0)
    input_feature = sel_col.text_input
