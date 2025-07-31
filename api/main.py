from fastapi import FastAPI
from api.simulator import simulate_payment

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "PushPaySim API is live!"}

@app.post("/simulate")
def run_simulation():
    result = simulate_payment()
    return result
