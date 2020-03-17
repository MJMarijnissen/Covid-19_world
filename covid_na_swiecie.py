# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:25:42 2020

@author: Kubus
"""

import pandas as pd
from datetime import datetime
import numpy as np


wczoraj = datetime.today().day-1
miesiac = datetime.today().month
rok = datetime.today().year-2000

url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
df = pd.read_csv(url, error_bad_lines=False)


def check(dzien, mies, rok):
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
	df = pd.read_csv(url, error_bad_lines=False)
	result = df.loc[df["Country/Region"]=="Poland"][f"{mies}/{dzien}/{rok}"].values[0]
	print(result)
	

def top(dzien, mies, rok):
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
    data= f"{mies}/{dzien}/{rok}"
    result = df[["Province/State", "Country/Region", data]].sort_values(by=data).tail(10)
    print(result)

print(f"data: {wczoraj}/{miesiac}")
print(f"przypadki w Polsce: ")
check(wczoraj, miesiac,rok)

print("miejsca z największą liczbą przypadków: ")
top(wczoraj,miesiac,rok)