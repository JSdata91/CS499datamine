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

Teacher_lst = []

#=======================
# Main

mysql_conn = PyMyConnection("admin", "admin")

#Read all student's GPA
teachers = mysql_conn.read_allTeachers()
for teach in teachers:
    teacherName =  teach.get('firstName') + ',' + teach.get('lastName')
    teacherPay = teach.get('salary')
    teacherRate = teach.get('rating')  
    teacherYears = teach.get('yearsEmployeed')  #need to fix name
    Teacher_lst.append([teacherName, teacherPay, teacherRate, teacherYears])  
    

#=======================
#Generate Scatter Plots
def ScatterOnTeacherRaitingPay():
    x = []
    y = []
    for tlist in Teacher_lst:
        x.append(tlist[1])
        y.append(tlist[2])
    
    colors = 'green'
    area = 22
    
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.title('Teacher Rating vs Pay')
    plt.xlabel('Pay')
    plt.ylabel('Student Rating')
    plt.show()
    
def ScatterOnTeacherPayYears():
    x = []
    y = []
    for tlist in Teacher_lst:
        x.append(tlist[3])
        y.append(tlist[1])
    
    colors = 'orange'
    area = 22
    
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.title('Teacher Pay vs Years Employed')
    plt.xlabel('Years Employed')
    plt.ylabel('Pay')
    plt.show()
    
def ScatterOnTeacherRaitingYears():
    x = []
    y = []
    for tlist in Teacher_lst:
        x.append(tlist[3])
        y.append(tlist[2])
    
    colors = 'teal'
    area = 22
    
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.title('Teacher Rating vs Years Employed')
    plt.xlabel('Years Employed')
    plt.ylabel('Student Rating')
    plt.show()

ScatterOnTeacherRaitingPay()
ScatterOnTeacherRaitingYears()
ScatterOnTeacherPayYears()