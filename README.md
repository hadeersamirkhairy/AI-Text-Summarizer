# AI Text Summarizer

An AI-powered text summarization web application built with Python and Flask, integrated with IBM watsonx.ai and the Granite Large Language Model (LLM).

The application allows users to submit text through a web interface and receive concise, AI-generated summaries in three clear bullet points.

## Live Demo

**Try the application:** https://ai-text-summarizer-inky.vercel.app/

## Features

- AI-powered text summarization.
- Integration with IBM watsonx.ai.
- Powered by the IBM Granite LLM (`ibm/granite-4-h-small`).
- Generates summaries in three clear bullet points.
- Simple and responsive web interface.
- Input validation and error handling.
- Secure API credential management using environment variables.
- Automated unit testing with Python unittest.
- Test coverage measurement using Coverage.py.
- Deployed on Vercel.

## Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Flask |
| AI Platform | IBM watsonx.ai |
| Language Model | IBM Granite |
| Frontend | HTML, CSS |
| Testing | Python unittest |
| Code Coverage | Coverage.py |
| Deployment | Vercel |
| Version Control | Git & GitHub |

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

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/hadeersamirkhairy/AI-Text-Summarizer.git
```

### 2. Navigate to the project directory

```bash
cd AI-Text-Summarizer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 5. Install dependencies

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

**Security Note:** Never commit your `.env` file or expose API credentials in your source code or public repositories.

For production deployment, configure the same environment variables through the Vercel project settings.

## Run the Application Locally

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## Testing

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

## Deployment

The application is deployed on **Vercel** and connected to the GitHub repository.

The deployment uses environment variables to securely manage IBM watsonx.ai credentials.

**Live Application:** https://ai-text-summarizer-inky.vercel.app/

## Author

**Hadeer Samir**

Developed as a Python and Generative AI application project.