# test_project_pytest
this is a test project example with test elements organized using pytest mechanism

## verified running environment
1. python3.10.4 + windows32
2. python 2.7.18  + windows32

## how to run
1. pull the code under a working path
   using git clone https://github.com/SpringTang2021/test_project_pytest
   or 
   download zip file
   assume my working place is as follows: 
   D:\dev_box\test_project_pytest>
   
2. run pytest under 
   * run the whole test project: 
     D:\dev_box\test_project_pytest> pytest
   
   * run one group of test project
      D:\dev_box\test_project_pytest> pytest test_project\group_function_name1
   
   * run one test suite in a group
     D:\dev_box\test_project_pytest> pytest  test_project\group_function_name1\test_function_name1_x1>test_function_name1_x1_suite1.py
 
 ## about logging
 1. command line log output
 2. log file with name of running datetime under test_logs
 
