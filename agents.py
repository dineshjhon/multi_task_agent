import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

load_dotenv()
model = os.getenv("MODEL")

# ✅ Summarizer
summarizer = Agent(
    name="summarizer",
    model=model,
    instruction="Summarize the given text clearly and concisely."
)

# ✅ QA Agent
qa_agent = Agent(
    name="qa_agent",
    model=model,
    instruction="Answer the user's question clearly and accurately."
)

# ✅ Classifier
classifier = Agent(
    name="classifier",
    model=model,
    instruction="""
    Classify the given text into one of:
    Positive, Negative, Neutral.

    Return ONLY the label.
    """
)

# ✅ Support Router
support_router = Agent(
    name="support_router",
    model=model,
    instruction="""
    Categorize the request into:
    Billing Support, Technical Support, General Support.

    Return ONLY the category.
    """
)

# ✅ ROOT AGENT (REAL BRAIN)
root_agent = Agent(
    name="root_agent",
    model=model,
    instruction="""
    You are a smart AI assistant that routes tasks to the correct specialist agent.

    Available agents:
    - summarizer → for summarizing text
    - qa_agent → for answering questions
    - classifier → for sentiment classification
    - support_router → for customer support categorization

    Rules:
    - Understand the user's intent
    - Select the best agent
    - Delegate the task
    - Return ONLY the final answer (not reasoning)

    Be accurate and concise.
    """,
    sub_agents=[
        summarizer,
        qa_agent,
        classifier,
        support_router
    ]
)