# Project Name

Brief description of your web app.

## Tech Stack
- Python (Flask / FastAPI)
- [Add your frontend/db here]

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repo
```bash
   git clone git@github-linux:linux-username/repo-name.git
   cd repo-name
```

2. Create and activate virtual environment
```bash
   # Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Set up environment variables
```bash
   cp .env.example .env
   # Then fill in your actual values in .env
```

5. Run the app
```bash
   # Flask
   flask run

   # FastAPI
   uvicorn main:app --reload
```

## Environment Variables
See `.env.example` for all required variables.