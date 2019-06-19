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
            json.load(self.client.get("/")),
            json.dumps({
                "status": "analytics server online"
            })
        )

    @unittest.skipIf(os.getenv("UNITTESTS_FAST_RUN") != None, "Fast run on")
    def test_key_creation(self):
        data = json.load(self.client.get("/keys/new"))
        self.tempauth = [
            data['result']['auth']['key'],
            data['result']['auth']['private-key']
        ]
        for i, z in enumerate(self.tempauth):
            self.assertIsNotNone(self.tempauth[i])

    @unittest.skipIf(os.getenv("UNITTESTS_FAST_RUN") != None, "Fast run on")
    def test_key_connection(self):
        for i in range(18):
            jdata = json.load(self.client.get("/connect", params={"key": self.tempauth[0]})),
            self.assertIn(
                jdata['result']
                json.dumps({
                    "result": {"fail": false}
                })
            )

    @unittest.skipIf(os.getenv("UNITTESTS_FAST_RUN") != None, "Fast run on")
    def test_key_deletion(self):
        self.assertEqual(
            json.load(self.client.get("/keys/delete", params={"key": self.tempauth[0], "private": self.tempauth[1]})),
            json.dumps({
                "result": {
                    "fail": false
                }
            })
        )


if __name__ == '__main__':
    unittest.main()
