# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 23:25:29 2021

@author: John Shumway
"""

import sys
import os
sys.path.append(os.getcwd() + '/..')

#import test cases
import TestStudent
import TestTeacher
import TestClass

# Init Test Cases
CaseStudent = TestStudent.TestCaseStudent()
CaseTeacher = TestTeacher.TestCaseTeacher()
CaseClass = TestClass.TestCaseClass()

#Run Tests
CStudentResult = CaseStudent.RunTest()
CTeacherResult = CaseTeacher.RunTest()
CClassResult = CaseClass.RunTest()