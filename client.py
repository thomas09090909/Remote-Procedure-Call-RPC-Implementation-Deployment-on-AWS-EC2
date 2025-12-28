import socket
import json
import uuid
import time

SERVER_IP = "<server-private-ip>"  # замените на приватный IP node-B
PORT = 5000
TIMEOUT = 2  # секунды
MAX_RETRIES = 3

def rpc_call(method, params):
    request_id = str(uuid.uuid4())
    request = {"request_id": request_id, "method": method, "params": params}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            s = socket.socket()
            s.settimeout(TIMEOUT)
            s.connect((SERVER_IP, PORT))
            s.send(json.dumps(request).encode())
            response = s.recv(1024).decode()
            s.close()
            return json.loads(response)
        except socket.timeout:
            print(f"Timeout! Retrying request {attempt}/{MAX_RETRIES} ...")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            s.close()
    return {"request_id": request_id, "result": None, "status": "FAILED"}

# Example usage
if __name__ == "__main__":
    print("Calling add(5,7)")
    response = rpc_call("add", {"a": 5, "b": 7})
    print("Response:", response)

    print("Calling reverse_string('hello')")
    response = rpc_call("reverse_string", {"s": "hello"})
    print("Response:", response)
