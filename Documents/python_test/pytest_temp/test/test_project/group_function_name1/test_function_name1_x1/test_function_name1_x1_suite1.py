#!/usr/bin/python
import os
import pytest
import logging
import common_lib
import biz_lib

class TestFunctionName1X1Class:
    
    @pytest.fixture(scope="class", autouse=True)
    def suite_setup_fixture(self, prj_fixture_info, suite_fixture_info, request):
        '''
        suite setup is to build the basic fixture env for all the test cases in this suite
        which can use the fixture info (eg: prj_fixture_info) setup when project setup
        '''
        logging.info("begin run suite setup fixture for class %s"%self.__class__.__name__)
       
        '''
        do suite setup here
        '''
        logging.info(prj_fixture_info.get_service_http_addr())
        logging.info(prj_fixture_info.get_service_rpc_addr())
        
        suite_fixture_info.append(5)
        
        '''
        add suite teardown which is to be run after all the test cases are to be finished
        '''
        def suite_teardown():
            logging.info("begin run suite teardown for class %s"%self.__class__.__name__)
            suite_fixture_info = [] 
            logging.info("suite_teardown suite_fixture_info =%s"%suite_fixture_info) 
        request.addfinalizer(suite_teardown)
        
    
    @pytest.fixture(scope="class")  
    def suite_fixture_info(self):
        return []      
        
                
    def test_f1(self, suite_fixture_info, request):
        '''
        this case is to verity the variable updated in suite setup
        '''
        logging.info("begin run test case %s"%request.node.name)
        logging.info("test_f1 suite_fixture_info =%s"%suite_fixture_info) 
        assert(suite_fixture_info == [5])

    def test_f2(self, suite_fixture_info, request):
        logging.info("begin run test case %s"%request.node.name)
        logging.info("test_f2 suite_fixture_info =%s"%suite_fixture_info )
        assert(suite_fixture_info == [3])

    
    def test_f3(self, request):
        '''
        this case is to verify assert equal rewrite for class Foo
        '''
        logging.info("begin run test case %s"%request.node.name)
        foo1 = biz_lib.Foo(1)
        foo2 = biz_lib.Foo(1)
        assert(foo1 == foo2)
         
    
    