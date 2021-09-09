# 1. import
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image
from multiapp import MultiPage
from apps import home, TPE30Data, TPE48Data, PVCData, KneeBraceData

st.markdown("""
# Multi-Page App
""")

app = MultiPage()
app.add_page('Home', home.app)
app.add_page('TPE30 Keywords', TPE30Data.app)
app.add_page('TPE48 Keywords', TPE48Data.app)
app.add_page('PVC Keywords', PVCData.app)
app.add_page('Knee Brace Keywords', KneeBraceData.app)
app.run()


