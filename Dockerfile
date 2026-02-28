FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000
ENV GUNICORN_WORKERS=4
ENV GUNICORN_CMD_ARGS="--bind 0.0.0.0:${PORT} --workers ${GUNICORN_WORKERS}"


EXPOSE 5000
CMD ["gunicorn", "run:app"]