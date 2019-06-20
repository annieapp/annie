import unittest
import logging
import sys
import os
from lcbools import true, false

try:
    import server
except ImportError:
    raise OSError("Failed to import the server module. Have you installed it?")

class Tests(unittest.TestCase):
    """
    The test class.
    
    .. important:: if you want to run CI-only tests, set the CI environment variable to 'yes'
    """
    def setUp(self):
        """
        The method called by each test before it starts.

        :return: nothing
        """
        self.tested_keys = []
        self.app = server.application
        self.app.config['TESTING'] = True

    def test_env(self):
        """
        Test that enviornment is correctly setup.

        :return: nothing
        :raises AssertionError:
        """
        self.assertTrue(self.app.config['TESTING'])
        
    def test_key_generation(self):
        """
        Test that keys can be generated and the length is correct.

        :return: nothing
        :raises AssertionError:
        """
        self.assertEqual(len(server.genkey()), 15)

    @unittest.skipIf(os.getenv("CI") == None, "Not in CI")
    def test_key_generation_randomness(self):
        """
        Test if keys are random enough.
        It does so by generating keys in bulk
        (1,000,000 to be exact), and makes sure
        that none of the keys match.

        .. warning:: This test can be hard on your system, proceed with caution

        That is why it is marked as CI only.

        :return: nothing
        :raises AssertionError:
        """
        for i in range(1000000):
            tmp = server.genkey()
            self.assertIsNotNone(tmp)
            if len(self.tested_keys) > 2:
                for p, l in enumerate(self.tested_keys):
                    self.assertNotEqual(tmp, self.tested_keys[p])
                    self.tested_keys.append(tmp)
        
    def test_lowercase_boolean_values(self):
        """
        Test that lcbools works.

        :return: nothing
        :raises AssertionError:
        """
        self.assertTrue(true)
        self.assertFalse(false)

    def test_logger(self):
        """
        Test that the logger is correctly setup.

        :return: nothing
        :raises AssertionError:
        """
        self.assertIsInstance(self.app.logger, logging.Logger)
        self.assertIsNotNone(self.app.logger)

    @unittest.skipIf(os.getenv("CI") == None, "Not in CI")
    def test_logger_in_ci(self):
        """
        Test if the logger can have working handlers.

        .. warning:: This test can mess with loggers in production

        That is why it is marked as CI only.

        :return: nothing
        :raises AssertionError:
        """
        self.app.logger.setLevel(logging.DEBUG)
        self.assertEqual(self.app.logger.getEffectiveLevel(), logging.DEBUG)
        self.app.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.assertTrue(self.app.logger.hasHandlers())


if __name__ == '__main__':
    unittest.main()
