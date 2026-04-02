import socket
import streamlit as st

HOST = '10.1.0.193'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def classify(event):
    if "ERROR" in event:
        return "HIGH"
    elif "WARNING" in event:
        return "MEDIUM"
    else:
        return "LOW"

st.title("📡 Network Event Monitoring System")

node = st.text_input("Enter Node ID")
event = st.text_input("Enter Event")

if st.button("Send Event"):
    if node and event:
        message = f"{node}: {event}"
        client.sendto(message.encode(), (HOST, PORT))

        level = classify(event)

        # Color output
        if level == "HIGH":
            st.error(f"{node} → {event} (HIGH)")
        elif level == "MEDIUM":
            st.warning(f"{node} → {event} (MEDIUM)")
        else:
            st.success(f"{node} → {event} (LOW)")