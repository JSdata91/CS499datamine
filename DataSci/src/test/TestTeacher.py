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

class TestCaseTeacher(object):
    def __init__(self):
        # ==================================
        # Init Database connection
        # TODO: better security in password
        self.my_sqlconnector = PyMyConnection('admin', 'admin')
        self.checklst = []
        
    def RunTest(self): 
        # ==================================
        #Test Teacher creation
        teacher_FName = 'Nancy'
        teacher_LName = 'Teacher'
        
        # ==================================
        #Create Test Cases.   Insert the new Teacher, then read the db on the new index to confirm the data is correct
        TC_createTeacher = self.my_sqlconnector.create_teacher(teacher_LName, teacher_FName)
        TC_readTeacher = self.my_sqlconnector.read_table_byID("teachers", TC_createTeacher.newId)
        self.checklst.append(TC_createTeacher)
        self.checklst.append(TC_readTeacher)
        
        string_correct_json = "{{'id': {idnum}, 'lastName': 'Teacher', 'firstName': 'Nancy'}}".format(idnum = TC_createTeacher.newId)
        
        # ===================================
        # Check results of tests.
        
        flg_Test_Result = True
        
        if TC_readTeacher.json == string_correct_json:
            print('Teacher Tests Successful!')
            return flg_Test_Result 
        else:
            print('Error found with Teacher Tests!')
            print('   JSON: ' + TC_readTeacher.json)
            print('   Correct Answer: ' + string_correct_json)  
        
            flg_Test_Result = False
            return flg_Test_Result             
