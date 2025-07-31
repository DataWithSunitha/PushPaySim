import streamlit as st
import requests

st.title("💸 PushPaySim Dashboard")

if st.button("Run Payment Simulation"):
    response = requests.post("http://localhost:8000/simulate")
    data = response.json()
    st.metric("Latency (ms)", data["latency_ms"])
    st.metric("Fraud Score", data["fraud_score"])
    st.metric("Approved", "✅" if data["approved"] else "❌")
