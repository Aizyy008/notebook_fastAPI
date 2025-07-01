# FastAPI Notebook Project

This project is a simple FastAPI web application using Jinja2 templates and static files.

## Prerequisites
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fast_api_notebook
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi jinja2 uvicorn
   ```

## Running the Project

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

- Open your browser and go to: [http://127.0.0.1:8000/items/1](http://127.0.0.1:8000/items/1)

## Project Structure

- `main.py` - Main FastAPI application
- `templates/` - Jinja2 HTML templates
- `static/` - Static files (CSS, JS, images)
- `env/` - Python virtual environment (should not be committed)

## Notes
- Make sure to activate your virtual environment before running the server.
- You can change the port or host in the `uvicorn` command as needed. 