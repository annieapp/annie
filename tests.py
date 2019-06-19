import unittest
import logging
import json
from flask import Response
try:
    import server
except ImportError:
    raise OSError("Failed to import the server module. Have you installed it?")

class Tests(unittest.TestCase):
    def setUp(self):
        self.app = server.application

    def test_key_generation(self):
        self.assertEqual(len(server.application.genkey()), 15)

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
            self.app.public_key_error()
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
            self.app.private_key_error()
        )

    def test_logger(self):
        self.assertIsInstance(self.app.logger, logging.Logger)
        self.assertIsNotNone(self.app.logger)


if __name__ == '__main__':
    unittest.main()
