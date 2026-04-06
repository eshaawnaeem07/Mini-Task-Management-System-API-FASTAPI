FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]