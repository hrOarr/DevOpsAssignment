FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY app.py .

ARG APP_COMMIT=unknown
ENV APP_COMMIT=${APP_COMMIT}

EXPOSE 5000
CMD ["python", "app.py"]