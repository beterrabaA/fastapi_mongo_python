FROM python:3.9-slim

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

EXPOSE 8080

CMD ["uvicorn", "fastapi:app", "--host", "0.0.0.0", "--port", "8080"]