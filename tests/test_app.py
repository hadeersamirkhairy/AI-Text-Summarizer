
import unittest
from unittest.mock import patch
from app import app


class TestSummarizer(unittest.TestCase):

    @patch("app.summarize_text")
    def test_ai_error(self, mock_summarize):

        # Simulate IBM API failure
        mock_summarize.side_effect = Exception("Simulated API error")

        client = app.test_client()

        response = client.post(
            "/summarize",
            data={"text": "This is a sample text."}
        )

        # Verify error response
        self.assertEqual(response.status_code, 502)
        self.assertIn(
            b"Unable to generate summary",
            response.data
        )

        mock_summarize.assert_called_once_with(
            "This is a sample text."
        )

    @patch("app.summarize_text")
    def test_successful_summary(self, mock_summarize):

        # Simulate a successful AI response
        mock_summarize.return_value = "AI improves healthcare."

        client = app.test_client()

        response = client.post(
            "/summarize",
            data={"text": "Artificial intelligence helps doctors."}
        )

        # Verify successful HTTP response
        self.assertEqual(response.status_code, 200)

        # Verify summary appears on the page
        self.assertIn(
            b"AI improves healthcare.",
            response.data
        )

        # Verify AI received the correct input
        mock_summarize.assert_called_once_with(
            "Artificial intelligence helps doctors."
        )

    @patch("app.summarize_text")
    def test_empty_input(self, mock_summarize):

        client = app.test_client()

        response = client.post(
            "/summarize",
            data={"text": ""}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b"Please enter some text!",
            response.data
        )

        # Verify AI was not called
        mock_summarize.assert_not_called()

    @patch("app.summarize_text")
    def test_whitespace_input(self, mock_summarize):

        client = app.test_client()

        response = client.post(
            "/summarize",
            data={"text": "     "}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b"Please enter some text!",
            response.data
        )

        # Verify AI was not called
        mock_summarize.assert_not_called()

    def test_home_page(self):

        client = app.test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
