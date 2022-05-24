import logging
import traceback
import functools
from os.path import dirname, realpath

def log_begin_end(func):
    '''
    add begin and end log message for a test case, 
    which is effective in python3 when fixture is also be  used in pytest
    '''
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            logging.getLogger().info("begin run %s/%s"%(func.__module__,  func.__name__))    
            func(*args, **kwargs)
        except Exception as exp:
            logging.getLogger().error("exception type is:%s"%type(exp))
            logging.getLogger().error(traceback.format_exc())
            raise
        finally:        
            logging.getLogger().info("end run %s/%s"%(func.__module__ ,  func.__name__))
    return wrapper_func


def get_group_name(file_path):
    '''
      example: file_path = 'C:\\users\\tang\\documents\\python_test'
    '''
    
    group_name = dirname(realpath(file_path)).split('\\')[-1]
    return group_name