import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

load_dotenv()
model = os.getenv("MODEL")

# Summarizer
summarizer = Agent(
    name="summarizer",
    model=model,
    instruction="Summarize the given text clearly.",
)

# QA Agent
qa_agent = Agent(
    name="qa_agent",
    model=model,
    instruction="Answer the question clearly.",
)

# Classifier
classifier = Agent(
    name="classifier",
    model=model,
    instruction="""
    Classify text into:
    Positive, Negative, Neutral
    """,
)

# Support Router
support_router = Agent(
    name="support_router",
    model=model,
    instruction="""
    Categorize into:
    Billing Support, Technical Support, General Support
    """,
)

# Router Agent (Main Brain)
router_agent = Agent(
    name="router",
    model=model,
    instruction="""
    Decide task type:
    summarize, qa, classify, route

    Return ONLY one word.
    """
)