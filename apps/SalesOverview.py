import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px
from PIL import Image
from Sales_Data import Clean_Sales_Data, Filter_Sales_Data, Organize_Sales_Data
from Ads_Data import Clean_Ads_Data, Filter_Ads_Data, Organize_Ads_Data

def app():
    dataset = st.container()

    with dataset:
        st.title("Sales Overview")
        df = pd.read_csv('./Data/SalesData/81211018883.txt', sep='\t')
        #st.dataframe(df)

    # data cleaning
    Clean_Sales_Data(df).format_datetime()
    Clean_Sales_Data(df).fillna_with_0()
    Clean_Sales_Data(df).generate_pst_dt()
    Clean_Sales_Data(df).generate_pst_wk()
    Clean_Sales_Data(df).generate_pfl()
    df_sd = df

    # data filtering
    df_sd_amz = Filter_Sales_Data(df_sd).filter_amz_order()
    df_sd_amz_paid = Filter_Sales_Data(df_sd_amz).filter_paid_order()
    # print(sd_amz_paid)

    # generate daily data
    df_sd_pfl_d = Organize_Sales_Data(df_sd_amz_paid).group_order_by_pfl_d()



    # data grouping
    df_sd_pfl_wk = Organize_Sales_Data(df_sd_amz_paid).group_order_by_pfl_wk()


    # plot data
    st.header('**Daily Orders**')
    st.dataframe(df_sd_pfl_d)
    bar_chart_pfl_d = px.bar(df_sd_pfl_d,
                       x='purchase-date-pst',
                       y='quantity',
                       color = 'portfolio'
                       )
    st.plotly_chart(bar_chart_pfl_d)

    st.header('**Weekly Orders**')
    st.dataframe(df_sd_pfl_wk)
    bar_chart_pfl_wk = px.bar(df_sd_pfl_wk,
                       x='purchase-week-pst',
                       y='quantity',
                       color = 'portfolio'
                       )
    bar_subchart_pfl_wk = px.bar(df_sd_pfl_wk,
                       x='purchase-week-pst',
                       y='quantity',
                                facet_row = 'portfolio',
                                 height=(1000)
                       )

    st.plotly_chart(bar_chart_pfl_wk)
    st.plotly_chart(bar_subchart_pfl_wk)