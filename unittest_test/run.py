# -*- coding:utf-8 -*-
import unittest
from unittest_test.demo_test import suite
from log_test.log import get_logger


logger = get_logger("unittest", "./logs", "test.log")


if __name__ == '__main__':
    logger.info("======== unittest result ========")
    with open('./logs/test.log', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = runner.run(suite)
    if not result.wasSuccessful():
        logger.error(f"unittest failures = {result.failures}")
