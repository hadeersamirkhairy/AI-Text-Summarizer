# AI Text Summarizer

A Flask-based AI Text Summarization web application powered by IBM watsonx.ai and the Granite LLM.

The application allows users to submit text and receive AI-generated summaries through a simple web interface.

## Features

- AI-powered text summarization.
- Integration with IBM watsonx.ai and Granite LLM.
- Flask-based web application.
- Input validation and error handling.
- Secure API credential management using environment variables.
- Automated unit testing.
- Test coverage measurement using Coverage.py.

## Tech Stack

- Python
- Flask
- IBM watsonx.ai
- Granite LLM
- HTML & CSS
- Python unittest
- Coverage.py

## Project Structure

```text
AI-Text-Summarizer/
│
├── app.py
├── ai_service.py
├── test_connection.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── tests/
    ├── test_app.py
    └── test_ai_service.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hadeersamirkhairy/AI-Text-Summarizer.git
```

2. Navigate to the project directory:

```bash
cd AI-Text-Summarizer
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment (Windows):

```bash
.venv\Scripts\activate
```

5. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root directory and configure your IBM watsonx.ai credentials:

```env
IBM_API_KEY=your_api_key
IBM_PROJECT_ID=your_project_id
IBM_URL=your_watsonx_endpoint
```

**Important:** Never upload your `.env` file or expose your API credentials.

## Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## Run Tests

Run the automated test suite:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Run tests with coverage:

```bash
python -m coverage run --source=app,ai_service -m unittest discover -s tests -p "test_*.py" -v
```

Generate the coverage report:

```bash
python -m coverage report -m
```

## Author

Developed as a Python and Generative AI application project.