import unittest
import logging
import os
import json
from lcbools import true, false

try:
    import server
except ImportError:
    raise OSError("Failed to import the server module. Have you installed it?")

class Tests(unittest.TestCase):
    def setUp(self):
        self.app = server.application
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_env(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_basic_app_values(self):
        self.assertIsNotNone(self.client)
        
    def test_key_generation(self):
        self.assertEqual(len(server.genkey()), 15)

    def test_lowercase_boolean_values(self):
        self.assertTrue(true)
        self.assertFalse(false)

    def test_logger(self):
        self.assertIsInstance(self.app.logger, logging.Logger)
        self.assertIsNotNone(self.app.logger)

    @unittest.skipIf(os.getenv("UNITTESTS_FAST_RUN") != None, "Fast run on")
    def test_status_endpoint(self):
        self.assertEqual(
            json.load(self.client.get("/").data.decode('utf-8')),
            json.dumps({
                "status": "analytics server online"
            })
        )


if __name__ == '__main__':
    unittest.main()
