import unittest
import logging
import json
from lcbools import true, false
from flask import Response

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

    def test_common_errors(self):
        self.assertEqual(
            Response(
                json.dumps({
                    "result": {
                        "fail": true,
                        "message": "Invalid or missing public key"
                    }
                }),
                mimetype='application/json'
            ),
            server.public_key_error()
        )
        self.assertEqual(
            Response(
                json.dumps({
                    "result": {
                        "fail": true,
                        "message": "Invalid or missing private key"
                    }
                }),
                mimetype='application/json'
            ),
            server.private_key_error()
        )

    def test_logger(self):
        self.assertIsInstance(self.app.logger, logging.Logger)
        self.assertIsNotNone(self.app.logger)


if __name__ == '__main__':
    unittest.main()
