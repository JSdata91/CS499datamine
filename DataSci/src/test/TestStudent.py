# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:18:56 2021

@author: John Shumway
"""

import sys
import os
sys.path.append(os.getcwd() + '/..')

from sqlconnector import PyMyConnection
from TestMessage import TestMessage

class TestCaseStudent(object):
    def __init__(self):
        # ==================================
        # Init Database connection
        # TODO: better security in password
        self.my_sqlconnector = PyMyConnection('admin', 'admin')
        self.checklst = []
        
    def RunTest(self):
        # ==================================
        #Test Student creation
        student_FName = 'Joe'
        student_LName = 'McTest'
        student_GPA = 2.6
        
        # ==================================
        #Create Test Cases.   Insert the new student, then read the db on the new index to confirm the data is correct
        TC_createStudent = self.my_sqlconnector.create_student(student_LName, student_FName, student_GPA)
        TC_readStudent = self.my_sqlconnector.read_table_byID("students", TC_createStudent.newId)
        self.checklst.append(TC_createStudent)
        self.checklst.append(TC_readStudent)
        

        # ===================================
        # Check results of tests.
        
        flg_Test_Result = True
        string_correct_json = "{{'id': {idnum}, 'LastName': 'McTest', 'FirstName': 'Joe', 'GPA': 2.6}}".format(idnum = TC_createStudent.newId)
             
        #If the result matches the correct string, return TRUE. Otherwise, show the mis-match result.
        if TC_readStudent.json == string_correct_json:
            print('Student Tests Successful!')
            return flg_Test_Result 
        else:
            print('Error found with Student Tests!')
            print('JSON: ' + TC_readStudent.json)
            print('Correct Answer: string_correct_json')  
            flg_Test_Result = False
            return flg_Test_Result           
