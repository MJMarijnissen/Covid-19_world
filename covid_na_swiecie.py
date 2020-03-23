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

url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"

df = pd.read_csv(url, error_bad_lines=False)

def format_date(date: datetime.date):
    """
    Helper function, converts date format to used in url. Works with differnt OS

    Parameters
    ----------
    date : datetime.date
        datetime object ex. datetime.date(2020, 3, 22)

    Returns
    -------
    TYPE STR
        Date in the form of string with proper formating

    """
    if os.name == "nt":
        return date.strftime('%#m/%#d/%y')
    else:
        return date.strftime('%-m/%-d/%y')


def check_poland(date: datetime.date):
    """
    Number of confirmed cases in Poland for given date

    Parameters
    ----------
    date : datetime.date
        datetime object ex. datetime.date(2020, 3, 22)

    Returns
    -------
    result : INT
        number of cases in Poland

    """
    date = format_date(date)
    result = df.loc[df["Country/Region"]=="Poland"][date].values[0]
    return result
	

def top(date: datetime.date):
    """
    Places with most confirmed cases

    Parameters
    ----------
    date : datetime.date
        datetime object ex. datetime.date(2020, 3, 22)
   
    Returns
    -------
    result : Pandas.DataFrame
        columns: index nr, Province/State, Country/Region, date for top 15 countries

    """
    date = format_date(date)
    result = df[["Province/State", "Country/Region", date]].sort_values(by=date).tail(15)
    return result
    

def brak_wirusa(date: datetime.date):
    """
    Places with no cases up till this date

    Parameters
    ----------
    date : datetime.date
        datetime object ex. datetime.date(2020, 3, 22)

    Returns
    -------
    TYPE Pandas DataFrame
        Returns DataFrame of countries unaffected

    """
    date = format_date(date)
    return df.loc[df[date]==0]

def draw_circle_world_map(date: datetime.date):
    """
    Creates circle world map of cases around the world. Map comes in .html

    Parameters
    ----------
    date : datetime.date
        datetime object ex. datetime.date(2020, 3, 22)

    Returns
    -------
    .html file. Open in browser to view

    """
    date = format_date(date)
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


if __name__ == '__main__':
    print(f"For date: {wczoraj}")
    print(f"Cases in Poland: {check_poland(wczoraj)}")
    
    print("Top Country/Regions: ")
    print(top(wczoraj))
    print('drawing map')
    draw_circle_world_map(wczoraj)