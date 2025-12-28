import socket
import json
import uuid
import time
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000

# Remote functions
def add(a, b):
    return a + b

def reverse_string(s):
    return s[::-1]

FUNCTIONS = {
    "add": add,
    "reverse_string": reverse_string
}

print("RPC Server ready on port 5000...")
server = socket.socket()
server.bind((HOST, PORT))
server.listen(5)

while True:
    conn, addr = server.accept()
    try:
        data = conn.recv(1024).decode()
        if not data:
            conn.close()
            continue

        request = json.loads(data)
        print(f"[{datetime.now()}] Received: {request} from {addr}")

        # Simulate artificial delay for Task 3
        time.sleep(5)

        request_id = request.get("request_id", str(uuid.uuid4()))
        method = request.get("method")
        params = request.get("params", {})

        if method in FUNCTIONS:
            result = FUNCTIONS[method](**params)
            response = {"request_id": request_id, "result": result, "status": "OK"}
        else:
            response = {"request_id": request_id, "result": None, "status": "ERROR: Unknown method"}

        conn.send(json.dumps(response).encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
