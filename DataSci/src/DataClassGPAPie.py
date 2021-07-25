# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:11:19 2021

@author: John Shumway
"""

from sqlconnector import PyMyConnection
import matplotlib.pyplot as plt
import numpy as np

#=======================
# Pre-setup

majors_lst = []
labels = []
sizes = []

file1 = open('../lib/Majors.txt', 'r')
Lines = file1.readlines()

count = 0
#Create a row of GPA counts for each major.  Strip the return character.
for line in Lines:
    if line not in majors_lst:        
        majors_lst.append([line.rstrip(), 0])
        labels.append(line)

#sort results
majors_lst.sort()

#=======================
# Main

    
def PieCharPerGPA(minGPA, maxGPA, title):
    
    mysql_conn = PyMyConnection("admin", "admin")

    #Read all student's GPA
    students = mysql_conn.read_studentGPA()
    for st in students:
        #get ID of Major name
        index = 0
        for major in majors_lst:
            if st.get('Major') == major[0]:
                break
            else:
                index += 1     
        
        #Check Student's GPA and add if within limits
        GPA = st.get('GPA')
        if (GPA <= maxGPA and GPA >= minGPA):
            majors_lst[index][1] = majors_lst[index][1] + 1


    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    for majorGPA in majors_lst:    
        sizes.append(majorGPA[1])  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=120, radius=1.8)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
    plt.title(title, size=8, bbox={'facecolor':'0.8', 'pad':5})
    fig = plt.gcf()
    fig.set_size_inches(6,5.5)
    fig.tight_layout()
    plt.show()
#dataGraph(res_dct, category_names)
PieCharPerGPA(3, 4, 'Majors with students of GPA between 3 and 4')

