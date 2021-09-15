import pandas as pd
import openpyxl
import time

class Clean_SP__Data:
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