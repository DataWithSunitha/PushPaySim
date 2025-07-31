import random
import time

def simulate_payment():
    latency_ms = random.randint(100, 1000)
    time.sleep(latency_ms / 1000.0)

    fraud_score = random.random()
    approved = fraud_score < 0.85  # Simple rule: approve if score < 0.85

    return {
        "latency_ms": latency_ms,
        "fraud_score": round(fraud_score, 2),
        "approved": approved
    }
