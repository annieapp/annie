import unittest
import logging
from flask import Response
try:
    import server
except ImportError:
    raise OSError("Failed to import the server module. Have you installed it?")
except ModuleNotFoundError:
    raise OSError("Failed to import the server module. Have you installed it?")

class Tests(unittest.TestCase):
    def setUp(self):
        self.app = server.application

    def key_generation(self):
        self.assertEqual(len(self.app.genkey()), 15)

    def common_errors(self):
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

    def logger(self):
        self.assertIsInstance(self.app.logger, logging.Logger)
        self.assertNotNone(self.app.logger)


if __name__ == '__main__':
    unittest.main()
