# syntax=docker/dockerfile:1
FROM python:3.11-slim
WORKDIR /app
COPY homework4.py ./
CMD ["python", "homework4.py"]