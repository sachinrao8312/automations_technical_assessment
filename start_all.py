import subprocess
import os
import signal

# Paths to your backend and frontend directories
backend_dir = "/home/sachin/automations_technical_assessment/backend"
frontend_dir = "/home/sachin/automations_technical_assessment/frontend"

# Start Uvicorn server in the backend directory
print("Starting Uvicorn server in the backend folder...")
uvicorn_process = subprocess.Popen(
    ["uvicorn", "main:app", "--reload"],
    cwd=backend_dir,
)

# Start NPM server in the frontend directory
print("Starting NPM server in the frontend folder...")
npm_process = subprocess.Popen(
    ["npm", "start"],
    cwd=frontend_dir,
)

# Start Redis server
print("Starting Redis server...")
redis_process = subprocess.Popen(["redis-server"])

try:
    # Keep script running until interrupted
    print("All servers are running. Press Ctrl+C to stop.")
    while True:
        pass
except KeyboardInterrupt:
    print("Stopping all servers...")
    # Terminate all processes
    uvicorn_process.terminate()
    npm_process.terminate()
    redis_process.terminate()

    # Ensure all processes are killed
    uvicorn_process.wait()
    npm_process.wait()
    redis_process.wait()
    print("All servers stopped.")
