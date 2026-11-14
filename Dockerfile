# Lunch Scraper v4: FastAPI + HTMX. Scrapes daily menus, caches them, serves them to the home hub.
FROM python:3.12-slim
WORKDIR /srv
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=Europe/Prague DATA_DIR=/data
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY lunch ./lunch
COPY tests ./tests
EXPOSE 8000
CMD ["uvicorn", "lunch.main:app", "--host", "0.0.0.0", "--port", "8000"]
