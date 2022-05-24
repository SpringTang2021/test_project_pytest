#!/usr/bin/python
import os
import pytest
import logging

class TestFunctionName2XX1Class:
    cls_items = []
    
    @pytest.fixture(scope="class", autouse=True)
    def suite_setup_fixture(self, request):
        logging.info("begin run suite setup fixture for class %s"%self.__class__.__name__)
       
        '''
        do suite setup
        '''
        request.addfinalizer(self.suite_teardown)
        self.cls_items = [5]
    
   
    def suite_teardown(self):
        logging.info("begin run suite teardown fixture for class %s"%self.__class__.__name__)
        self.cls_items = []       
        
    def test_f2_xx1_case1(self, request):
        logging.info("begin run test case %s"%request.node.name)
        assert(self.cls_items == [5])
        
    
    def test_f2_xx1_case2(self, request):
         logging.info("begin run test case %s"%request.node.name)
         assert(self.cls_items == [4])
         
    
    