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
    def setUp(self):
        self.app = server.application
        self.app.config['TESTING'] = True

    def test_env(self):
        self.assertTrue(self.app.config['TESTING'])
        
    def test_key_generation(self):
        self.assertEqual(len(server.genkey()), 15)

    def test_lowercase_boolean_values(self):
        self.assertTrue(true)
        self.assertFalse(false)

    def test_logger(self):
        self.assertIsInstance(self.app.logger, logging.Logger)
        self.assertIsNotNone(self.app.logger)

    @unittest.skipIf(os.getenv("CI") == None, "Not in CI")
    def test_logger_in_ci(self):
        app.logger.setLevel(logging.DEBUG)
        self.assertEqual(app.logger.getEffectiveLevel(), logging.debug)
        app.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.assertTrue(app.logger.hasHandlers())


if __name__ == '__main__':
    unittest.main()
