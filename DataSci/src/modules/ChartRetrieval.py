# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:56:42 2021

@author: John Shumway
"""

import sys
import os
sys.path.append(os.getcwd() + '/..')
sys.path.append(os.getcwd() + '/../test')

from sqlconnector import PyMyConnection


mysql_conn = PyMyConnection("admin", "admin")
in_user_group = input("Enter group code to find Charts: ")

if in_user_group is not None:
    chart_results = mysql_conn.read_charts_by_group(in_user_group)
    
    
#Have user select chart
print("Select chart to use:")
x = 1
for result in chart_results:
    print(str(x) + ": " + result.get("FileName") + " " + str(result.get("UploadDate")) )
    x += 1
    
in_user_selection = int(input("chart: "))
in_user_selection -= 1  #reduce value by 1 for list
print("Getting file data...")

#Get the filedata for the selected item
if int(in_user_selection) > 0: 
    selected_data = chart_results[int(in_user_selection)]
