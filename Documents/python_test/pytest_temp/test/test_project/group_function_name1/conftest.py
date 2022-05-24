import pytest
import logging
import common_lib

@pytest.fixture(scope="package", autouse=True)
def group_fixture():
    logging.getLogger().info("begin run group fixture for  %s"%common_lib.get_group_name(__file__))    
    return 3