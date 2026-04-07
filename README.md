# Network Event Monitoring System (UDP-Based)

## Overview

This project implements a **UDP-based network event monitoring system**.
It consists of:

* A **server** that listens for incoming events, classifies them, filters low-priority logs, and aggregates counts.
* A **client UI (Streamlit)** that allows users to send events to the server.

The system demonstrates key Computer Networks concepts such as:

* UDP communication
* Client-server architecture
* Event classification and filtering
* Basic log aggregation

---

## Project Structure

```
.
├── server.py                  # UDP server for receiving and processing events
├── client_ui_streamlit.py     # Streamlit UI client for sending events
├── generate_cert.py           # (Optional) Certificate generation script
├── server.crt                 # Certificate file
├── server.key                 # Private key file
```

---

## How It Works

### Server (2nd Computer)

* Runs on the **2nd computer**
* Listens on a specific IP and port
* Receives messages in format:

  ```
  node_id: event_message
  ```
* Performs:

  * **Classification**

    * ERROR → HIGH
    * WARNING → MEDIUM
    * Others → LOW
  * **Filtering**

    * LOW events are ignored
  * **Aggregation**

    * Counts occurrences of each event
  * **Logging**

    * Displays time, node, event, level, and count

---

### Client (1st Computer)

* Runs on the **1st computer**
* Uses Streamlit UI to send events
* Sends UDP packets to the server IP

---

## Setup Instructions

### 1. Install Python

Make sure Python 3.8+ is installed on both computers.

### 2. Install Dependencies

Run on the 1st computer:

```
pip install streamlit
```

---

## Configuration

### IP Address Setup

In `client_ui_streamlit.py` (1st computer):

```
HOST = 'IP_OF_2ND_COMPUTER'
```

In `server.py` (2nd computer):

```
HOST = '0.0.0.0'
```

---

## How to Run

### Step 1: Start Server (2nd Computer)

```
python server.py
```

Expected output:

```
[STARTED] UDP Server running on <IP>:5000
```

---

### Step 2: Run Client (1st Computer)

```
streamlit run client_ui_streamlit.py
```

This will open a browser UI.

---

## Usage Instructions

1. Enter:

   * **Node ID** (e.g., Node1, RouterA)
   * **Event** (e.g., ERROR Disk Failure)

2. Click **Send Event**

3. Behavior:

   * Event is sent to server via UDP
   * Server processes and prints output

---

## Example

### Input (Client)

```
Node: Node1
Event: ERROR Disk Failure
```

### Server Output

```
[12:30:15] Node1 → ERROR Disk Failure | Level: HIGH | Count: 1
```

---

## Event Levels

| Event Type | Level  | Action       |
| ---------- | ------ | ------------ |
| ERROR      | HIGH   | Logged       |
| WARNING    | MEDIUM | Logged       |
| Others     | LOW    | Filtered out |

---

## Key Concepts Demonstrated

* UDP Socket Programming
* Real-time Logging
* Event Classification
* Filtering Mechanism
* Aggregation of Logs
* Simple Monitoring Dashboard

---

## Notes

* UDP is **connectionless**, so delivery is not guaranteed
* Ensure both computers are on the **same network** or reachable via IP
* Port `5000` must be open
* Firewall settings may affect communication

---

## Possible Improvements

* Add persistent logging (file/database)
* Add authentication/security
* Use TCP for reliability
* Dashboard for server logs
* Deploy on cloud

---

## Troubleshooting

### No messages received on server

* Check IP address in client
* Ensure server is running
* Check firewall settings

### Streamlit not opening

```
pip install streamlit
```

### Port issues

* Change port in both client and server if needed

---

## Authors

* Vyas PES2UG24CS569
* Yaseen PES2UG24CS607
* Vikas PES2UG24CS583

---

## Summary

This project simulates a basic **network monitoring system** where a client (1st computer) sends events to a server (2nd computer) that processes and filters logs efficiently.
