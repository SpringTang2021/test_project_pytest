import pytest
import sys
import logging
from os.path import dirname, realpath
sys.path.append(dirname(realpath(__file__)) + '/prj_lib/')
import project_common_lib  as prj_common_lib

@pytest.fixture(scope="session", autouse=True)
def prj_fixture_build(prj_fixture_info):
    '''
    the things that need to be done before test cases execution
    '''
    if not prj_common_lib.build_dev_code():
        logging.getLogger().warning("build dev code failed")
        pytest.exit("build dev code failed, triggered exit", 2)
    else:
        logging.getLogger().info("build dev code succeed")
    if not prj_common_lib.run_unit_test():
        logging.getLogger().warning("run unit test for dev code failed")
        pytest.exit("run unit test for dev code failed, triggered exit", 2)
    else:
        logging.getLogger().info("run unit test for dev code succeed")
    
    prj_fixture_info.set_service_http_addr("http://10.0.0.27:10086")
    prj_fixture_info.set_service_rpc_addr("10.0.0.27:10087")
    

@pytest.fixture(scope="session")
def prj_fixture_info():
    logging.getLogger().info("begin call prj_fixture_info")
    return  prj_common_lib.ProjectFixtureInfo()
        
        
        
    