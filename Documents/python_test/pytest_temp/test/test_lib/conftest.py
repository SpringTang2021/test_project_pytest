import logging
from biz_lib import Foo

def pytest_assertrepr_compare(op, left, right):
    logging.getLogger().info("begin run pytest_assertrepr_compare")
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]