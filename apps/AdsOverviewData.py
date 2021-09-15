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
def app():
    dataset = st.container()

    with dataset:
        st.title("Ads Overview")
        df = pd.read_excel('./Data/TargetingReport/Targeting report 0615-0913.xlsx')
        #st.dataframe(df)

    Clean_Ads_Data(df).delete_columns_space()
    Clean_Ads_Data(df).fillna_with_0()


    Clean_Ads_Data(df).generate_wk()
    df_grouped_day = Organize_Ads_Data(df).data_pfl_day()
    df_grouped_week = Organize_Ads_Data(df).data_pfl_wk()
    df_cpg_wk = Organize_Ads_Data(df).data_cpg_wk()
    df_targeting_wk = Organize_Ads_Data(df).data_tgt_wk()
    #st.dataframe(df)



# -----------------------------------------------------------------------------------------------------------
    st.header('**Daily Ads Data**')
    st.dataframe(df_grouped_day[funcyions_d])
    bar_chart_pfl_d = px.bar(df_grouped_day,
                       x='Date',
                       y='Impressions',
                       color = 'Portfolio name'
                       )
    bar_subchart_pfl_d = px.bar(df_grouped_day,
                       x='Date',
                       y='Impressions',
                                facet_row = 'Portfolio name',
                                height = (1000)
                       )

    bar_subchart_pflcpd_d = px.bar(df_grouped_day,
                                   x='Date',
                                   y='Spend',
                                   facet_row='Portfolio name',
                                   height=(1000)
                                   )

    line_chart_pflctr_d = px.line(df_grouped_day,
                       x='Date',
                       y='CTR',
                                 color='Portfolio name'
                       )
    line_chart_pflcvr_d = px.line(df_grouped_day,
                       x='Date',
                       y='CVR',
                                 color='Portfolio name'
                       )
    line_chart_pflcpc_d = px.line(df_grouped_day,
                       x='Date',
                       y='CPC',
                                 color='Portfolio name'
                       )
    line_chart_pflacos_d = px.line(df_grouped_day,
                       x='Date',
                       y='ACOS',
                                 color='Portfolio name'
                       )



    st.plotly_chart(bar_chart_pfl_d)
    st.plotly_chart(bar_subchart_pfl_d)
    st.plotly_chart(bar_subchart_pflcpd_d)
    st.plotly_chart(line_chart_pflctr_d)
    st.plotly_chart(line_chart_pflcvr_d)
    st.plotly_chart(line_chart_pflcpc_d)
    st.plotly_chart(line_chart_pflacos_d)

# -----------------------------------------------------------------------------------------------------------
    st.header('**Weekly Ads Data**')
    st.dataframe(df_grouped_week[funcyions_wk])
    bar_chart_pfl_wk = px.bar(df_grouped_week,
                       x='Week',
                       y='Impressions',
                       color = 'Portfolio name'
                       )
    bar_subchart_pfl_wk = px.bar(df_grouped_week,
                       x='Week',
                       y='Impressions',
                                 facet_row = 'Portfolio name',
                                 height=(1000)
                       )
    line_chart_pflctr_wk = px.line(df_grouped_week,
                       x='Week',
                       y='CTR',
                                 color='Portfolio name'
                       )
    line_chart_pflcvr_wk = px.line(df_grouped_week,
                       x='Week',
                       y='CVR',
                                 color='Portfolio name'
                       )

    bar_subchart_pflcpd_wk = px.bar(df_grouped_week,
                       x='Week',
                       y='Spend',
                                    facet_row = 'Portfolio name',
                                    height=(1000)
                       )
    line_chart_pflcpc_wk = px.line(df_grouped_week,
                       x='Week',
                       y='CPC',
                                 color='Portfolio name'
                       )
    line_chart_pflacos_wk = px.line(df_grouped_week,
                       x='Week',
                       y='ACOS',
                                 color='Portfolio name'
                       )
    st.plotly_chart(bar_chart_pfl_wk)
    st.plotly_chart(bar_subchart_pfl_wk)
    st.plotly_chart(bar_subchart_pflcpd_wk)
    st.plotly_chart(line_chart_pflctr_wk)
    st.plotly_chart(line_chart_pflcvr_wk)
    st.plotly_chart(line_chart_pflcpc_wk)
    st.plotly_chart(line_chart_pflacos_wk)


