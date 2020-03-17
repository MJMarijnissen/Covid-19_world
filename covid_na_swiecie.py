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

url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
df = pd.read_csv(url, error_bad_lines=False)


def check(dzien, mies):
	df = pd.read_csv(url, error_bad_lines=False)
	result = df.loc[df["Country/Region"]=="Poland"][f"{mies}/{dzien}/20"].values[0]
	print(result)
	
 

print(f"data: {wczoraj}/{miesiac}")
print("przypadki: ", check(wczoraj, miesiac))