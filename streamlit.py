# 1. import
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image
from multiapp import MultiPage
from apps import home, TPE30Data, TPE48Data, PVCData, KneeBraceData, SalesOverview, AdsOverviewData, AdsBreakdown
from google.oauth2 import service_account
from gsheetsdb import connect

st.markdown("""
 Multi-Page App
""")

app = MultiPage()
app.add_page('Home', home.app)
app.add_page('TPE30 Keywords', TPE30Data.app)
app.add_page('TPE48 Keywords', TPE48Data.app)
app.add_page('PVC Keywords', PVCData.app)
app.add_page('Knee Brace Keywords', KneeBraceData.app)
app.add_page('Sales Overview', SalesOverview.app)
app.add_page('Ads data Overview', AdsOverviewData.app)
app.add_page('Ads data Breakdown', AdsBreakdown.app)
app.run()


'''
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["private_gsheets_url"]
st.write(sheet_url);
rows = run_query(f'SELECT * FROM "{sheet_url}"')
st.write(rows);
#Print results.
for row in rows:
    st.write(row);
  #  st.write(f"{row.item-name} {row.item-description}:")
'''