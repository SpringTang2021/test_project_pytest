import logging

class TestFunctionName1X2Class:
    '''
    this test suite explicitly use xunit style setup/teardown instead of fixture
    '''
    class_f = -1

    @classmethod
    def setup_class(cls):
        logging.info("begin run test suite setup for class %s "%cls.__name__)
        cls.class_f = 3

    @classmethod
    def teardown_class(cls):
        logging.info("begin run test suite teardown for class %s "%cls.__name__)
        pass
    
    def setup_method(self, method):
        logging.info("begin run  test case setup  %s"%method.__name__)
        pass
        
    
    def teardown_method(self, method):
        logging.getLogger().info("begin run test case teardown %s"%method.__name__)
        pass

    def test_f1(self, request):
         logging.info("begin run test case %s"%request.node.name)
         assert(self.class_f == 3)

    def test_f2(self, request):
         logging.info("begin run test case %s"%request.node.name)
         assert(self.class_f == 4)
    