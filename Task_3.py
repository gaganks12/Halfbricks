# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:16:18 2020

@author: 61449
"""


import pandas as pd
import csv


#table_name='sandbox-installs'
print("This script will generate SQL insert statements for all the rows in the input")

print("Select file")
filename = input("Filename: ")
extension = filename.split(".")[-1].lower()
    
f_name = open(filename,encoding='utf8', errors='ignore')

if extension == "csv":
    data=pd.read_csv(f_name)
    for index, row in data.iterrows():
        print('INSERT INTO sandbox-installs' ' (''user_pseudo_id',',''sku',',''app_version',',''geo_country',','
                                            'geo_region',',''geo_city',',''install_source',',''ua_name',
                                            ',''ua_medium',',''ua_source',',''device_category',','
                                            'device_brand_name',',''device_model_name',','
                                            'device_os_hardware_model',',''device_os',','
                                            'device_os_version',',''idfa',',''idfv',','
                                            'is_limited_ad_tracking',',''device_language',','
                                            'device_time_zone_offset',',''timestamp_raw',','
                                            'table_date',',''is_returning_user',',''session_id' ')  VALUES ' +
                                            '(' + row['user_pseudo_id'],',',row['sku'],',',row['app_version'],',',
                                            row['geo_country'],',',row['geo_region'],',',row['geo_city'],',',
                                            row['install_source'],',',row['ua_name'],',',row['ua_medium'],',',
                                            row['ua_source'],',',row['device_category'],',',row['device_brand_name']
                                            ,',',row['device_model_name'],',',row['device_os_hardware_model'],',',
                                            row['device_os'],',',row['device_os_version'],',',row['idfa']
                                            ,',',row['idfv'],',',row['is_limited_ad_tracking'],',',row['device_language'],',',
                                            row['device_time_zone_offset'],',',row['timestamp_raw'],',',
                                            row['table_date'],',',row['is_returning_user'],',',row['session_id'] ,");") 
               
        print("\n")

