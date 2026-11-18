
import unittest
from unittest.mock import patch
from app import app


class TestSummarizer(unittest.TestCase):

    @patch("app.summarize_text")
    def test_ai_error(self, mock_summarize):

        # Simulate IBM API failure
        mock_summarize.side_effect = Exception("Simulated API error")

        # Send a fake POST request
        client = app.test_client()

        response = client.post(
            "/summarize",
            data={"text": "This is a sample text."}
        )

        # Check the response
        self.assertEqual(response.status_code, 502)

        self.assertIn(
            b"Unable to generate summary",
            response.data
        )

    @patch("app.summarize_text")
    def test_successful_summary(self, mock_summarize):

        # Simulate a successful AI response
        mock_summarize.return_value = "AI improves healthcare."

        # Create Flask test client
        client = app.test_client()

        # Simulate user submitting text
        response = client.post(
            "/summarize",
            data={"text": "Artificial intelligence helps doctors."}
        )

        # Verify successful HTTP response
        self.assertEqual(response.status_code, 200)

        # Verify the summary appears on the page
        self.assertIn(
            b"AI improves healthcare.",
            response.data
        )

    def test_empty_input(self):

        client = app.test_client()

        response = client.post(
            "/summarize",
            data={"text": ""}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Please enter some text!", response.data)

    def test_whitespace_input(self):
        client = app.test_client()

        response = client.post(
            "/summarize",
            data={"text": "     "}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Please enter some text!", response.data)
    def test_home_page(self):
        client = app.test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()


