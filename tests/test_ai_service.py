
import os
import unittest
from unittest.mock import patch

from ai_service import summarize_text


class TestAIService(unittest.TestCase):

    def test_missing_credentials(self):

        # Simulate missing IBM credentials
        empty_env = {
            "IBM_API_KEY": "",
            "IBM_PROJECT_ID": "",
            "IBM_URL": ""
        }

        with patch.dict(os.environ, empty_env):

            with self.assertRaisesRegex(
                ValueError,
                "Missing IBM credentials!"
            ):
                summarize_text("Test text")

    def test_successful_summary(self):

        # Simulate valid IBM credentials
        fake_env = {
            "IBM_API_KEY": "fake-api-key",
            "IBM_PROJECT_ID": "fake-project-id",
            "IBM_URL": "https://example.com"
        }

        expected_summary = "AI improves healthcare."

        fake_response = {
            "choices": [
                {
                    "message": {
                        "content": expected_summary
                    }
                }
            ]
        }

        with patch.dict(os.environ, fake_env):

            with patch("ai_service.Credentials") as mock_credentials:

                with patch("ai_service.ModelInference") as mock_model:

                    # Simulate AI response
                    mock_model.return_value.chat.return_value = fake_response

                    result = summarize_text(
                        "Artificial intelligence helps doctors."
                    )

                    # Verify returned summary
                    self.assertEqual(result, expected_summary)

                    # Verify model was initialized
                    mock_model.assert_called_once()

                    # Verify AI was called
                    mock_model.return_value.chat.assert_called_once()


if __name__ == "__main__":
    unittest.main()
