import os
import time
import psutil
from flask import Flask, jsonify

app = Flask(__name__)
START_TIME = time.time()

@app.get("/health")
def health():
    # Contract: always return 200 if process is alive and serving requests
    return jsonify(status="ok"), 200

@app.get("/metrics")
def metrics():
    uptime_seconds = int(time.time() - START_TIME)

    # psutil gives us real system stats from inside the container/host
    return jsonify(
        cpu_percent=psutil.cpu_percent(interval=0.1),
        memory_percent=psutil.virtual_memory().percent,
        uptime_seconds=uptime_seconds
    ), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "9000"))
    # 0.0.0.0 is required for Docker later
    app.run(host="0.0.0.0", port=port)