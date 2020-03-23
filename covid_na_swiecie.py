# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:25:42 2020

@author: Kubus
"""

import pandas as pd
import datetime
import numpy as np
import plotly.express as px
from plotly.offline import plot
import os


wczoraj = datetime.date.today() - datetime.timedelta(days=1)
# wczoraj = datetime.today().day-1
# miesiac = datetime.today().month
# rok = datetime.today().year-2000

url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
df = pd.read_csv(url, error_bad_lines=False)

# Helper function (strftime not cross platform) ???
def format_date(date: datetime.date):
    if os.name == "nt":
        return date.strftime('%#m/%#d/%y')
    else:
        return date.strftime('%-m/%-d/%y')


def check(date: datetime.date):
    """
    Sprawdza ile wystąpień wirusa jest w Polsce

    Parameters
    ----------
    dzien : INT
        Day of the year
    mies : INT
        Month of the year
    rok : INT
        Last 2 digits of year e.g. for 2020, write 20

    Returns
    -------
    None. Only prints results

    """
	#df = pd.read_csv(url, error_bad_lines=False)
    date = format_date(date)
    result = df.loc[df["Country/Region"]=="Poland"][date].values[0]
    print(result)
	

def top(date: datetime.date):
    """
    Zwraca miejsca z największą liczbą przypadkóW

    Parameters
    ----------
    dzien : INT
        Day of the year
    mies : INT
        Month of the year
    rok : INT
        Last 2 digits of year e.g. for 2020, write 20

    Returns
    -------
    None. Only prints results

    """
    date = format_date(date)
    result = df[["Province/State", "Country/Region", date]].sort_values(by=date).tail(10)
    print(result)
    

def brakwirusa(date: datetime.date):
    """
    brak przypadków do dannego dnia włącznie

    Parameters
    ----------
    dzien : INT
        Day of the year
    mies : INT
        Month of the year
    rok : INT
        Last 2 digits of year e.g. for 2020, write 20

    Returns
    -------
    TYPE Pandas DataFrame
        Returns DataFrame of countries unaffected

    """
    date = format_date(date)
    return df.loc[df[date]==0]

print(f"data: {wczoraj}")
print(f"przypadki w Polsce: ")
check(wczoraj)

print("miejsca z największą liczbą przypadków: ")
top(wczoraj)

formated_gdf = df.groupby(["Country/Region"]).max()
formated_gdf =  formated_gdf.reset_index()
date = format_date(wczoraj)
formated_gdf['size'] = formated_gdf[date].pow(0.3)
fig = px.scatter_geo(formated_gdf, locations="Country/Region", locationmode='country names', 
                     color=date, size="size", hover_name="Country/Region", 
                     range_color= [0, max(formated_gdf[date])+2], 
                     projection="natural earth", 
                     title=f"COVID-19 na swiecie w dniu {date}" 
                     )

plot(fig)