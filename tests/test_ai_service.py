
import os
import unittest
from unittest.mock import patch

from ai_service import summarize_text


class TestAIService(unittest.TestCase):

    def test_missing_credentials(self):

        # Test each missing credential separately
        credentials = {
            "IBM_API_KEY": "fake-api-key",
            "IBM_PROJECT_ID": "fake-project-id",
            "IBM_URL": "https://example.com"
        }

        for missing_key in credentials:

            with self.subTest(missing_key=missing_key):

                test_env = credentials.copy()
                test_env[missing_key] = ""

                with patch.dict(os.environ, test_env):

                    with self.assertRaisesRegex(
                        ValueError,
                        "Missing IBM credentials!"
                    ):
                        summarize_text("Test text")

    def test_successful_summary(self):

        fake_env = {
            "IBM_API_KEY": "fake-api-key",
            "IBM_PROJECT_ID": "fake-project-id",
            "IBM_URL": "https://example.com"
        }

        user_text = "Artificial intelligence helps doctors."
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

                    mock_model.return_value.chat.return_value = fake_response

                    result = summarize_text(user_text)

                    # Verify returned summary
                    self.assertEqual(result, expected_summary)

                    # Verify IBM credentials configuration
                    mock_credentials.assert_called_once_with(
                        api_key="fake-api-key",
                        url="https://example.com"
                    )

                    # Verify Granite model configuration
                    mock_model.assert_called_once_with(
                        model_id="ibm/granite-4-h-small",
                        credentials=mock_credentials.return_value,
                        project_id="fake-project-id"
                    )

                    # Verify AI received the correct prompt
                    expected_messages = [
                        {
                            "role": "user",
                            "content": (
                                "Summarize the following text in 3 clear bullet points. "
                                "Preserve important information. "
                                "Do not invent facts.\n\n"
                                f"Text:\n{user_text}"
                            )
                        }
                    ]

                    mock_model.return_value.chat.assert_called_once_with(
                        messages=expected_messages
                    )

    def test_api_error(self):

        fake_env = {
            "IBM_API_KEY": "fake-api-key",
            "IBM_PROJECT_ID": "fake-project-id",
            "IBM_URL": "https://example.com"
        }

        with patch.dict(os.environ, fake_env):

            with patch("ai_service.Credentials"):

                with patch("ai_service.ModelInference") as mock_model:

                    # Simulate IBM API failure
                    mock_model.return_value.chat.side_effect = RuntimeError(
                        "IBM API unavailable"
                    )

                    with self.assertRaisesRegex(
                        RuntimeError,
                        "IBM API unavailable"
                    ):
                        summarize_text("Test text")


if __name__ == "__main__":
    unittest.main()
