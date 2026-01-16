#!/usr/bin/env bash
set -euo pipefail

IMAGE="metrics-api:dev"
NAME="metrics-api"
HOST_PORT="${1:-9000}"
CONTAINER_PORT="5000"

# Stop existing container if it exists
docker rm -f "$NAME" >/dev/null 2>&1 || true

# Run container
docker run --rm -d \
  -p "${HOST_PORT}:${CONTAINER_PORT}" \
  -e PORT="${CONTAINER_PORT}" \
  --name "${NAME}" \
  "${IMAGE}"

echo "Running on: http://localhost:${HOST_PORT}"
echo "Health: http://localhost:${HOST_PORT}/health"
echo "Metrics: http://localhost:${HOST_PORT}/metrics"