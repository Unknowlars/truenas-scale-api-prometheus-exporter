FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN groupadd --system truenas && useradd --system --gid truenas --create-home --home-dir /app truenas

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY --chown=truenas:truenas truenas_exporter.py /app/truenas_exporter.py

USER truenas

EXPOSE 9108

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import os, urllib.request; port = os.getenv('EXPORTER_PORT', '9108'); urllib.request.urlopen(f'http://127.0.0.1:{port}/healthz', timeout=3).read()"

CMD ["python", "/app/truenas_exporter.py"]
