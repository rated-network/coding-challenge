from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import random
import time
from typing import List

app = FastAPI()

DELAY_INJECTION_RATE = 0.05  # 5% of requests will be delayed
DELAY_TIME = 0.25 # Delay time in seconds

# Fault rates for each 1K requests
FAULT_RATES: List[float] = [
  0.001,
  0.02,
  0.003,
  0.1,
  0.0,
  0.005,
  0.2,
  0.01,
  0.001
]

# Request counter
request_count = 0

@app.get("/entities")
async def read_root():
    global request_count
    request_count += 1

    # Determine the current fault rate
    fault_rate = FAULT_RATES[min(request_count // 1000, len(FAULT_RATES) - 1)]

    # Inject delays randomly
    if random.random() < DELAY_INJECTION_RATE:
        time.sleep(DELAY_TIME)

    # Inject faults randomly
    if random.random() < fault_rate:
        print("Oh no! Fault injected!")
        raise HTTPException(status_code=500, detail="Injected fault")

    return {"message": "Hello, World!", "request_count": request_count, "fault_rate": fault_rate}

@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
