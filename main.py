from fastapi import FastAPI
from pydantic import BaseModel
from agents import root_agent

app = FastAPI()

class RequestModel(BaseModel):
    input: str

@app.post("/process")
def process(req: RequestModel):

    result = root_agent.run(req.input)

    return {
        "result": result
    }