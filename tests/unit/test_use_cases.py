from src.main import create_app
import unittest
from mock import patch
import json
import os

with open(
    os.path.join(os.path.dirname(__file__), "events", "new_publication.json")
) as file:
    data = json.load(file)


app = create_app()


class FlaskTest(unittest.TestCase):
    @patch("test_app.connect_db")
    def test_root(self):
        response = app.test_client().post(
            "/api/v1/post/123",
            data=data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
