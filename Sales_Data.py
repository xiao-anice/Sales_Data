import pandas as pd
import openpyxl
import time

class Clean_Sales_Data:
    def __init__(self, df):
        self.df = df

    def fillna_with_0(self):
        self.df = self.df.fillna(0)
        return self.df

    def format_datetime(self):
        self.df['last-updated-date'] = pd.to_datetime(self.df['last-updated-date'])
        self.df['purchase-date'] = pd.to_datetime(self.df['purchase-date'])
        return self.df


    def generate_pst_dt(self):
        self.df['purchase-datetime-pst'] = self.df['purchase-date'].dt.tz_convert(tz='Etc/GMT+8')
        self.df['purchase-date-pst'] = self.df['purchase-datetime-pst'].dt.strftime('%Y-%m-%d')
        self.df['purchase-time-pst'] = self.df['purchase-datetime-pst'].dt.strftime('%H:%M:%S')
        #print(self.df)
        return self.df

    def generate_pst_wk(self):
        self.df['purchase-week-pst'] = self.df['purchase-datetime-pst'].dt.isocalendar().week
        #print(self.df)
        return self.df

    def generate_pfl(self):
        self.df['portfolio'] = self.df['sku'].map({
            'GGKB27SBK': 'Knee Brace',
            'GGKB27MBK': 'Knee Brace',
            'GGKB27LBK': 'Knee Brace',
            'TG6401-BKUS': 'PVC',
            'BLUE-GRAY-648': 'PVC',
            'PURPLE-GRAY-648': 'PVC',
            'TG6401-BKUS-NEW': 'NEW-PVC',
            'Yoga-646': 'TPE-48',
            'GG625BKTPEUS': 'TPE-30'})
        #print(self.df)
        return self.df



class Filter_Sales_Data:
    def __init__(self, df):
        self.df = df

    def filter_amz_order(self):
        df_amz = self.df[self.df['sales-channel'] != 'Non-Amazon']
        #print(self.df_amz)
        return df_amz

    def filter_paid_order(self):
        df_paid = self.df[self.df['order-status'] != 'Cancelled']
        #print(self.df_paid)
        return df_paid

class Organize_Sales_Data:
    def __init__(self, df):
        self.df = df

    def group_order_by_d(self):
        df_order_daily = self.df.groupby(['purchase-date-pst'],as_index=False).sum()
        #print(self.df_order_daily)
        return df_order_daily

    def group_order_by_wk(self):
        df_order_weekly = self.df.groupby(['purchase-week-pst'],as_index=False).sum()
        #print(self.df)
        return df_order_weekly

    def group_order_by_pfl_d(self):
        df_order_pfl_daily = self.df.groupby(['purchase-date-pst', 'portfolio'], as_index=False).quantity.sum()
        return df_order_pfl_daily

    def group_order_by_pfl_wk(self):
        df_order_pfl_weekly = self.df.groupby(['purchase-week-pst', 'portfolio'], as_index=False).quantity.sum()
        return df_order_pfl_weekly





