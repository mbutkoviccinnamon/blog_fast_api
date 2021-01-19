FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY app.py db.py main.py models.py schema.py __init__.py requirements.txt .env ./app/

RUN pip install -r app/requirements.txt