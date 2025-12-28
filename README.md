
# Remote-Procedure-Call-RPC-Implementation-Deployment-on-AWS-EC2

# RPC Demo — How to Run

## Prerequisites
- Two AWS EC2 instances (Ubuntu 22.04 LTS)
  - rpc-server-node (node-B)
  - rpc-client-node (node-A)
- Security group allowing TCP port 5000 between nodes
- Python 3 installed on both instances
- SSH access using labsuser.pem key

## Running the Server (node-B)
1. SSH into the server:
ssh -i labsuser.pem ubuntu@<server-public-ip>
2. Install Python 3 (if not installed):
sudo apt update
sudo apt install python3 python3-pip -y
3. Run the server:
python3 server.py
Expected output:
RPC Server ready on port 5000...

## Running the Client (node-A)
1. SSH into the client:
ssh -i labsuser.pem ubuntu@<client-public-ip>
2. Update client.py with the private IP of node-B
3. Run the client:
python3 client.py
Example output:
Calling add(5,7)
Response: {'request_id': '...', 'result': 12, 'status': 'OK'}
Calling reverse_string('hello')
Response: {'request_id': '...', 'result': 'olleh', 'status': 'OK'}

## Optional: Demonstrate Failure Handling
- In server.py, add:
time.sleep(5)  # simulate server delay
- Run client while server is delayed. Client retries will show:
Timeout! Retrying request 1/3 ...
- RPC Semantics: at-least-once
