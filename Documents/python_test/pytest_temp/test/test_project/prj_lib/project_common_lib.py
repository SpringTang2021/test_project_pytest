import sys
import os
import logging

def build_dev_code():
    logging.getLogger().info("begin run project build_dev_code")
    '''
    do build dev code here
    if build succeed, return True, otherwise return False
    '''
    return True

def run_unit_test():
    logging.getLogger().info("begin run unit test for dev code")
    '''
    do run unit test here
    if unit test succeed, return True, otherwise return False
    '''
    return True

class ProjectFixtureInfo:
    def __init__(self):
        self.service_http_addr = ""
    
    def set_service_http_addr(self, service_http_addr):
        logging.getLogger().info("begin call %s::set_service_http_addr with params %s"%(self.__class__, service_http_addr))
        self.service_http_addr  = service_http_addr
    
    def set_service_rpc_addr(self, service_rpc_addr):
        logging.getLogger().info("begin call %s::set_service_rpc_addr with params %s"%(self.__class__, service_rpc_addr))
        self.service_rpc_addr  = service_rpc_addr
    
    def get_service_http_addr(self):
        logging.getLogger().info("begin call get_service_http_addr")
        return self.service_http_addr    

    def get_service_rpc_addr(self):
        logging.getLogger().info("begin call get_service_rpc_addr")
        return self.service_rpc_addr