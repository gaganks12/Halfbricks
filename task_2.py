# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:48:17 2020

@author: 61449
"""

import os
import csv
import json
from collections import OrderedDict
import pandas as pd


print("This script will give data description")

print("Select file")
filename = input("Filename: ")
extension = filename.split(".")[-1].lower()
    
f_name = open(filename,encoding='utf8', errors='ignore')

if extension == "csv":
    data=pd.read_csv(f_name)
    x_3=data.describe()
    x_1=data['device_brand_name'].value_counts().head(10)
    x_2=data['device_category'].value_counts()
    x_4=data.groupby(['geo_country']).size()
    x_5=data.groupby('device_category')['device_brand_name'].value_counts()
    x_6=data['device_language'].value_counts().head(10)

    print("Data Description:\n",x_3)
    print("top 10 device brands are:\n", x_1)
    print("Total count of Device categories are:\n",x_2)
    print("Count of each country:\n", x_4)
    print('Categorised based on device category:', x_5)
    print("top 10 highest used languages:", x_6)
    
    
        
    
        