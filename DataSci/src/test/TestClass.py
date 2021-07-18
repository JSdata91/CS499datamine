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

class TestCaseClass(object):
    def __init__(self):
        # ==================================
        # Init Database connection
        # TODO: better security in password
        self.my_sqlconnector = PyMyConnection('admin', 'admin')
        self.checklst = []
        
    def RunTest(self):
        # ==================================
        #Test Class creation
        class_Name = 'Programming 101'
        student_id = 28
        teacher_id = 4
        
        # ==================================
        #Create Test Cases.   Insert the new Class, then read the db on the new index to confirm the data is correct
        TC_createClass = self.my_sqlconnector.create_class(class_Name, str(student_id), str(teacher_id) )
        TC_readClass = self.my_sqlconnector.read_table_byID("classes", TC_createClass.newId)
        self.checklst.append(TC_createClass)
        self.checklst.append(TC_readClass)
        
        string_correct_json = "{{'id': {idnum}, 'studentid': 28, 'teacherid': 4, 'className': 'Programming 101'}}".format(idnum = TC_createClass.newId)
        
        # ===================================
        # Check results of tests.
        
        flg_Test_Result = True
        
        if TC_readClass.json == string_correct_json:
            print('Class Tests Successful!')
            return flg_Test_Result
        else:
            print('Error found with Class Tests!')
            print('   JSON: ' + TC_readClass.json)
            print('   Correct Answer: ' + string_correct_json)  
    
            flg_Test_Result = False
            return flg_Test_Result          
