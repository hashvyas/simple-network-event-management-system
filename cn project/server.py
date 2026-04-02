import socket
import datetime

HOST = '127.0.0.1'
PORT = 5000

# Store event counts
event_count = {}

def classify_event(event):
    if "ERROR" in event:
        return "HIGH"
    elif "WARNING" in event:
        return "MEDIUM"
    else:
        return "LOW"

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))

    print(f"[STARTED] UDP Server running on {HOST}:{PORT}")

    while True:
        try:
            data, addr = server.recvfrom(1024)
            message = data.decode()

            time = datetime.datetime.now().strftime("%H:%M:%S")

            # Extract node and event
            if ":" in message:
                node, event = message.split(":", 1)
                node = node.strip()
                event = event.strip()
            else:
                node = "UNKNOWN"
                event = message.strip()

            # Classification
            level = classify_event(event)

            # Filtering (ignore LOW events)
            if level == "LOW":
                print(f"[{time}] {node} → {event} | FILTERED (LOW)")
                continue

            # Aggregation
            if event not in event_count:
                event_count[event] = 0

            event_count[event] += 1

            # Clean professional output
            print(f"[{time}] {node} → {event} | Level: {level} | Count: {event_count[event]}")

        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    start_server()