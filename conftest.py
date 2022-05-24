import sys
import pytest
import traceback
import logging
from datetime import datetime
from os.path import dirname, realpath
sys.path.append(dirname(realpath(__file__)) + '/test_lib/')

def pytest_configure(config):
    """ 
    this is a pytest hook.
    create a log file if log_file is not configured in command line and in *.ini file
    """
    if not config.option.log_file and not config.getini("log_file"):
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = 'test_logs/pytest_logs-.' + timestamp + ".log"

def pytest_exception_interact(report):
    """
    this is a hook to log test exception
    """
    logging.error('!!! test exception:\n %s'%report.longreprtext)

