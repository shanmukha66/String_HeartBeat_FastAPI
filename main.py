from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Define the input model
class TextInput(BaseModel):
    text: str

# Heartbeat endpoint
@app.get("/heartbeat/{input_text}")
async def heartbeat(input_text: str):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": input_text, "timestamp": current_time}

# Version endpoint
@app.get("/version")
async def version():
    return {"version": "1.0.0"}

# ToUpper endpoint
@app.post("/to-upper")
async def to_upper(input_data: TextInput):
    return {"result": input_data.text.upper()}

# ToLower endpoint
@app.post("/to-lower")
async def to_lower(input_data: TextInput):
    return {"result": input_data.text.lower()} 