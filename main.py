from fastapi import FastAPI
from pydantic import BaseModel
from agents import router_agent, summarizer, qa_agent, classifier, support_router

app = FastAPI()

class RequestModel(BaseModel):
    input: str

@app.post("/process")
def process(req: RequestModel):

    # Step 1: Detect task
    task = router_agent.run(req.input).strip().lower()

    # Step 2: Route
    if "summarize" in task:
        result = summarizer.run(req.input)

    elif "qa" in task:
        result = qa_agent.run(req.input)

    elif "classify" in task:
        result = classifier.run(req.input)

    elif "route" in task:
        result = support_router.run(req.input)

    else:
        result = "Could not determine task"

    return {
        "task": task,
        "result": result
    }