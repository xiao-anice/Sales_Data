import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px
from PIL import Image
from Sales_Data import Clean_Sales_Data, Filter_Sales_Data, Organize_Sales_Data
from Ads_Data import Clean_Ads_Data, Filter_Ads_Data, Organize_Ads_Data

funcyions_d = ['Date', 'Portfolio name', 'Impressions', 'Clicks', 'Spend', 'CTR', 'CVR', 'ACOS','CPC']
funcyions_wk = ['Week', 'Portfolio name', 'Impressions', 'Clicks', 'Spend', 'CTR', 'CVR', 'ACOS','CPC']
functions_cpg_wk = ['Week', 'Campaign Name', 'Impressions', 'Clicks', 'Spend', 'CTR', 'CVR', 'ACOS','CPC', '7 Day Total Sales',
             '7 Day Total Orders (#)',
             '7 Day Total Units (#)',
             '7 Day Advertised SKU Units (#)',
             '7 Day Other SKU Units (#)',
             '7 Day Advertised SKU Sales',
             '7 Day Other SKU Sales']

# -----------------------------------------------------------------------------------------------------------
def app():
    dataset = st.container()

    with dataset:
        st.title("Ads Breakdown")
        df = pd.read_excel('./Data/TargetingReport/Targeting report 0615-0913.xlsx')
        #st.dataframe(df)

    Clean_Ads_Data(df).delete_columns_space()
    Clean_Ads_Data(df).fillna_with_0()


    Clean_Ads_Data(df).generate_wk()
    df_grouped_day = Organize_Ads_Data(df).data_pfl_day()
    df_grouped_week = Organize_Ads_Data(df).data_pfl_wk()
    df_cpg_wk = Organize_Ads_Data(df).data_cpg_wk()
    df_cpg_wk.fillna(0)
    df_targeting_wk = Organize_Ads_Data(df).data_tgt_wk()
    #st.dataframe(df)

    # plot data
    st.header('**Weekly TPE Campaign Data**')

    cpg_name = df_cpg_wk['Campaign Name'].unique().tolist()
    options = st.selectbox(
        'Choose the Campaign you want to analyze',
        cpg_name)

    # mask data

    mask = (df_cpg_wk['Campaign Name']== options)
    df_group1 = df_cpg_wk[mask]
    st.dataframe(df_group1[functions_cpg_wk])
    bar_chart_cpgimp_wk = px.bar(df_group1,
                       x='Week',
                       y='Impressions',
                              color='Campaign Name'
                       )

    bar_chart_cpgspd_wk = px.bar(df_group1,
                                   x='Week',
                                   y='Spend',

                                   )
    bar_chart_cpgorder_wk = px.bar(df_group1,
                                   x='Week',
                                   y='7 Day Total Orders (#)',

                                   )
    bar_chart_cpgsales_wk = px.bar(df_group1,
                                   x='Week',
                                   y='7 Day Total Sales',
                                   )

    line_chart_cpgcpg_wk = px.line(df_group1,
                       x='Week',
                       y='CTR',
                       )
    line_chart_cpgcvr_wk = px.line(df_group1,
                       x='Week',
                       y='CVR',

                       )
    line_chart_cpgcpc_wk = px.line(df_group1,
                       x='Week',
                       y='CPC',

                       )
    line_chart_cpgacos_wk = px.line(df_group1,
                       x='Week',
                       y='ACOS',

                       )

    st.plotly_chart(bar_chart_cpgimp_wk)
    st.plotly_chart(bar_chart_cpgspd_wk)
    st.plotly_chart(bar_chart_cpgorder_wk)
    st.plotly_chart(bar_chart_cpgsales_wk)
    st.plotly_chart(line_chart_cpgcpg_wk)
    st.plotly_chart(line_chart_cpgcvr_wk)
    st.plotly_chart(line_chart_cpgcpc_wk)
    st.plotly_chart(line_chart_cpgacos_wk)