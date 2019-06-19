import unittest
import logging
import json
from lcbools import true, false

try:
    import server
except ImportError:
    raise OSError("Failed to import the server module. Have you installed it?")

class Tests(unittest.TestCase):
    def setUp(self):
        self.app = server.application

    def test_key_generation(self):
        self.assertEqual(len(server.genkey()), 15)

    def test_lowercase_boolean_values(self):
        self.assertTrue(true)
        self.assertFalse(false)

    def test_logger(self):
        self.assertIsInstance(self.app.logger, logging.Logger)
        self.assertIsNotNone(self.app.logger)


if __name__ == '__main__':
    unittest.main()
