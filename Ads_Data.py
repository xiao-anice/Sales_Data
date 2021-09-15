import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import regex as re
from openpyxl import workbook
import pytz, datetime

functions = {'Impressions': 'sum',
             'Clicks': 'sum',
             'Spend': 'sum',
             '7 Day Total Sales': 'sum',
             '7 Day Total Orders (#)': 'sum',
             '7 Day Total Units (#)': 'sum',
             '7 Day Advertised SKU Units (#)': 'sum',
             '7 Day Other SKU Units (#)': 'sum',
             '7 Day Advertised SKU Sales': 'sum',
             '7 Day Other SKU Sales': 'sum',
             }

class Clean_Ads_Data:
    def __init__(self, df):
        self.df = df

    def fillna_with_0(self):
        self.df = self.df.fillna(0)
        return self.df

    def delete_columns_space(self):
        self.df = self.df.rename(columns=lambda x: x.strip(), inplace=True)
        return self.df

    def generate_wk(self):
        self.df['Week'] = self.df['Date'].dt.isocalendar().week
        #print(self.df)
        return self.df

class Filter_Ads_Data:
    def __init__(self, df):
        self.df = df


class Organize_Ads_Data:
    def __init__(self, df):
        self.df = df

    def data_pfl_day(self):
        df_pfl_day = self.df.groupby(['Date','Portfolio name'], as_index=False).agg(functions)
        df_pfl_day['CTR'] = df_pfl_day['Clicks']/df_pfl_day['Impressions']
        df_pfl_day['ACOS'] = df_pfl_day['Spend']/df_pfl_day['7 Day Total Sales']
        df_pfl_day['CVR'] = df_pfl_day['7 Day Total Orders (#)']/df_pfl_day['Clicks']
        df_pfl_day['CPC'] = df_pfl_day['Spend']/ df_pfl_day['Clicks']
        return df_pfl_day

    def data_pfl_wk(self):
        df_pfl_wk = self.df.groupby(['Week','Portfolio name'], as_index=False).agg(functions)
        df_pfl_wk['CTR'] =  df_pfl_wk['Clicks'] /  df_pfl_wk['Impressions']
        df_pfl_wk['ACOS'] =  df_pfl_wk['Spend']/ df_pfl_wk['7 Day Total Sales']
        df_pfl_wk['CVR'] =  df_pfl_wk['7 Day Total Orders (#)'] / df_pfl_wk['Clicks']
        df_pfl_wk['CPC'] = df_pfl_wk['Spend']/ df_pfl_wk['Clicks']
        return df_pfl_wk

    def data_cpg_day(self):
        df_cpg_day = self.df.groupby(['Date','Campaign Name'], as_index=False).agg(functions)
        df_cpg_day['CTR'] = df_cpg_day['Clicks']/df_cpg_day['Impressions']
        df_cpg_day['ACOS'] = df_cpg_day['Spend']/df_cpg_day['7 Day Total Sales']
        df_cpg_day['CVR'] = df_cpg_day['7 Day Total Orders (#)']/df_cpg_day['Clicks']
        df_cpg_day['CPC'] = df_cpg_day['Spend']/ df_cpg_day['Clicks']
        return df_cpg_day

    def data_cpg_wk(self):
        df_cpg_wk = self.df.groupby(['Week','Campaign Name'], as_index=False).agg(functions)
        df_cpg_wk['CTR'] =  df_cpg_wk['Clicks'] / df_cpg_wk['Impressions']
        df_cpg_wk['ACOS'] =  df_cpg_wk['Spend']/ df_cpg_wk['7 Day Total Sales']
        df_cpg_wk['CVR'] =  df_cpg_wk['7 Day Total Orders (#)'] / df_cpg_wk['Clicks']
        df_cpg_wk['CPC'] = df_cpg_wk['Spend']/ df_cpg_wk['Clicks']
        return df_cpg_wk

    def data_adsgroup_day(self):
        df_adsgrp_day = self.df.groupby(['Date','Ad Group Name'], as_index=False).agg(functions)
        df_adsgrp_day['CTR'] = df_adsgrp_day['Clicks']/df_adsgrp_day['Impressions']
        df_adsgrp_day['ACOS'] = df_adsgrp_day['Spend']/df_adsgrp_day['7 Day Total Sales']
        df_adsgrp_day['CVR'] = df_adsgrp_day['7 Day Total Orders (#)']/df_adsgrp_day['Clicks']
        df_adsgrp_day['CPC'] = df_adsgrp_day['Spend'] / df_adsgrp_day['Clicks']
        return df_adsgrp_day

    def data_adsgroup_wk(self):
        df_adsgrp_wk = self.df.groupby(['Week','Ad Group Name'], as_index=False).agg(functions)
        df_adsgrp_wk['CTR'] =  df_adsgrp_wk['Clicks'] / df_adsgrp_wk['Impressions']
        df_adsgrp_wk['ACOS'] =  df_adsgrp_wk['Spend']/ df_adsgrp_wk['7 Day Total Sales']
        df_adsgrp_wk['CVR'] =  df_adsgrp_wk['7 Day Total Orders (#)'] / df_adsgrp_wk['Clicks']
        df_adsgrp_wk['CPC'] = df_adsgrp_wk['Spend'] / df_adsgrp_wk['Clicks']
        return df_adsgrp_wk

    def data_tgt_day(self):
        df_tgt_day = self.df.groupby(['Date','Targeting', 'Match Type'], as_index=False).agg(functions)
        df_tgt_day['CTR'] = df_tgt_day['Clicks']/df_tgt_day['Impressions']
        df_tgt_day['ACOS'] = df_tgt_day['Spend']/df_tgt_day['7 Day Total Sales']
        df_tgt_day['CVR'] = df_tgt_day['7 Day Total Orders (#)']/df_tgt_day['Clicks']
        df_tgt_day['CPC'] = df_tgt_day['Spend'] / df_tgt_day['Clicks']
        return df_tgt_day

    def data_tgt_wk(self):
        df_tgt_wk = self.df.groupby(['Week','Targeting','Match Type'], as_index=False).agg(functions)
        df_tgt_wk['CTR'] =  df_tgt_wk['Clicks'] / df_tgt_wk['Impressions']
        df_tgt_wk['ACOS'] =  df_tgt_wk['Spend']/ df_tgt_wk['7 Day Total Sales']
        df_tgt_wk['CVR'] =  df_tgt_wk['7 Day Total Orders (#)'] / df_tgt_wk['Clicks']
        df_tgt_wk['CPC'] = df_tgt_wk['Spend'] / df_tgt_wk['Clicks']
        return df_tgt_wk


