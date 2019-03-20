import unittest

import app


class test_rest(unittest.TestCase):
    def setUp(self):
        client = app.create_app()
        self.client = client.test_client()

    def test_ok_status(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(b"ok" in res.data, True)

if __name__ == "__main__":
    unittest.main()
