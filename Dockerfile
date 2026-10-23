ARG PYTHON_VERSION=3.14.8

FROM python:${PYTHON_VERSION}-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /build
COPY requirements.txt /build/
RUN python -m pip wheel --wheel-dir /wheels -r requirements.txt
COPY pyproject.toml README.md LICENSE /build/
COPY src /build/src
RUN python -m pip wheel --no-deps --wheel-dir /wheels .

FROM python:${PYTHON_VERSION}-slim AS runtime

LABEL org.opencontainers.image.title="TrueNAS Prometheus Exporter" \
      org.opencontainers.image.description="Prometheus exporter for the TrueNAS SCALE JSON-RPC API" \
      org.opencontainers.image.source="https://github.com/Unknowlars/truenas-scale-api-prometheus-exporter" \
      org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN groupadd --system --gid 10001 truenas \
    && useradd --system --uid 10001 --gid 10001 --no-create-home truenas

COPY --from=builder /wheels /wheels
RUN python -m pip install /wheels/*.whl \
    && python -m pip uninstall --yes pip \
    && rm -rf /wheels

USER 10001:10001
WORKDIR /app

EXPOSE 9108

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import os, urllib.request; port = os.getenv('EXPORTER_PORT', '9108'); urllib.request.urlopen(f'http://127.0.0.1:{port}/healthz', timeout=3).read()"

ENTRYPOINT ["truenas-exporter"]
