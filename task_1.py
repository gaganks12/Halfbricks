# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:24:05 2020

@author: 61449
"""

import os
import csv
import json
from collections import OrderedDict


print("This script will convert a CSV file to JSON")

print("Select file")
filename = input("Filename: ")
extension = filename.split(".")[-1].lower()
    
f_name = open(filename,encoding="mbcs")

if extension == "csv":
    data = list(csv.reader(f_name))
    #print(data)
    keys = data[0]
    converted = []

    for i in range(1, len(data)):
        obj = OrderedDict()
        for j in range(0,len(keys)):
            if len(data[i][j]) > 0:
                obj[keys[j]] = data[i][j]
            else:
                obj[keys[j]] = None
                converted.append(obj)
    converted_basename = os.path.basename(filename).split(".")[0]
    converted_file_extension = ".json"
    
    try:
        if converted_file_extension == ".json":
            with open(converted_basename + converted_file_extension, 'w') as outfile:
                json.dump(converted, outfile)
        
    except:
        print("Error creating file ... exiting")
    else:
        print("File created:",converted_basename + converted_file_extension)

else:
    print("unsupported file type")
    exit()
    
