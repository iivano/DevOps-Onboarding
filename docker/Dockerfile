# ---------- Builder stage ----------
FROM python:3.11-slim AS builder

WORKDIR /wheels

# Build tools only live in the builder stage
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy requirements and build wheels for all deps
COPY app/requirements.txt /tmp/requirements.txt
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r /tmp/requirements.txt


# ---------- Runtime stage ----------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# curl for HEALTHCHECK only
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Install deps from prebuilt wheels (no gcc needed here)
COPY --from=builder /wheelz /wheels
RUN pip install --no-cache-dir /wheels/*

# Copy app code
COPY app/ /app/

ENV PORT=9000

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -fsS http://localhost:${PORT}/health || exit 1

CMD ["python", "app.py"]