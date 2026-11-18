
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()


def summarize_text(user_text):

    # Get IBM credentials
    api_key = os.getenv("IBM_API_KEY")
    project_id = os.getenv("IBM_PROJECT_ID")
    url = os.getenv("IBM_URL")

    if not all([api_key, project_id, url]):
        raise ValueError("Missing IBM credentials!")

    # Configure authentication
    credentials = Credentials(
        api_key=api_key,
        url=url
    )

    # Initialize Granite model
    model = ModelInference(
        model_id="ibm/granite-4-h-small",
        credentials=credentials,
        project_id=project_id
    )

    # Prepare the prompt
    messages = [
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

    # Send request to Granite
    response = model.chat(messages=messages)

    # Extract and return summary
    summary = response["choices"][0]["message"]["content"]

    return summary
