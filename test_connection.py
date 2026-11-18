
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

# Load environment variables
load_dotenv()

api_key = os.getenv("IBM_API_KEY")
project_id = os.getenv("IBM_PROJECT_ID")
url = os.getenv("IBM_URL")

# Check credentials
if not all([api_key, project_id, url]):
    raise ValueError("Missing IBM credentials!")

# Set up IBM authentication
credentials = Credentials(
    api_key=api_key,
    url=url
)

# Initialize the Granite model
model = ModelInference(
    model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=project_id
)

# Send our first prompt
messages = [
    {
        "role": "user",
        "content": (
            "Summarize this text in 2 bullet points: "
            "AI helps doctors analyze medical images. "
            "It also helps businesses automate repetitive tasks."
        )
    }
]

response = model.chat(messages=messages)

print("AI Summary:")
print(response["choices"][0]["message"]["content"])
