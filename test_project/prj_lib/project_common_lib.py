import sys
import os
import logging
import configparser
import project_common_var as prj_constant

class ProjectConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_parser  = None
        self.prj_basic_keys = []
        self.prj_dev_modules_keys = []
         
    def parse_prj_conf(self):
        logging.getLogger().info("begin run parse_prj_conf for %s"%self.config_file)
        if not os.path.exists(self.config_file):
            logging.error("prj conf file [%s] is not existed"%self.config_file)
            return False
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(self.config_file)
        self.prj_basic_keys = self.config_parser.options(prj_constant.PRJ_CONF_BASICS)
        self.prj_dev_modules_keys = self.config_parser.options(prj_constant.PRJ_CONF_DEV_MODULES)
        logging.info("prj_basic_keys=%s"%self.prj_basic_keys)
        logging.info("prj_dev_modules_keys =%s"%self.prj_dev_modules_keys)
        return True
    
    def get_basic_config(self):
        return self._get_config(prj_constant.PRJ_CONF_BASICS) 
    
    def get_dev_modules_config(self):
        return self._get_config(prj_constant.PRJ_CONF_DEV_MODULES)

    def _get_config(self, config_section_name):
        kv_map = {}
        option_keys = []
        if prj_constant.PRJ_CONF_BASICS == config_section_name:
            option_keys = self.prj_basic_keys
        elif prj_constant.PRJ_CONF_DEV_MODULES == config_section_name:
            option_keys  = self.prj_dev_modules_keys
        else:
            logging.warning("unknown section name [%s]"%config_section_name)
        for key in  option_keys:
            kv_map[key] = self.config_parser.get(config_section_name, key)
        logging.info("parse project config, items in [%s] are:%s"\
                             %(config_section_name, kv_map))
        return kv_map

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