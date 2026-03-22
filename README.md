# AI Agent System README

This document describes the structure and functionality of an AI agent system, focusing on the roles of its various components.

## Overview

This AI system is designed to process and respond to user queries by leveraging specialized agents. When a user interacts with the system, an initial `root_agent` triages the query and transfers it to the most appropriate specialized agent. This modular approach ensures that queries are handled efficiently and accurately by the agent best equipped for the task.

## Agents

The system comprises the following agents:

### 1. `root_agent`

*   **Description:** The primary entry point for all user interactions. It acts as a router, classifying incoming queries and delegating them to the most suitable specialized agent.
*   **Role:** Initial query reception and intelligent routing.

### 2. `qa_agent` (This Agent)

*   **Description:** The agent responsible for providing direct, accurate answers to specific factual questions. It specializes in understanding queries and retrieving or generating informative responses.
*   **Role:** Answering direct questions and providing explanations.
*   **Example Use:** When a user asks "What is AI?", the `root_agent` transfers the query to the `qa_agent` for a detailed explanation.

### 3. `summarizer`

*   **Description:** This agent is designed to condense longer texts, articles, or conversations into shorter, coherent summaries, extracting key information and main points.
*   **Role:** Text summarization.
*   **Example Use:** If a user requests "summarize the below article," the query is routed to the `summarizer`.

### 4. `classifier`

*   **Description:** An agent focused on categorizing user input or data into predefined classes or types. It helps in understanding the intent or topic of a query.
*   **Role:** Input classification and intent recognition.

### 5. `support_router`

*   **Description:** This agent specializes in handling support-related queries. It can route support requests to appropriate human or automated support channels, or provide initial self-help information.
*   **Role:** Managing and routing support inquiries.

## How it Works

1.  **User Input:** A user initiates an interaction with the system.
2.  **`root_agent` Evaluation:** The `root_agent` receives the input and analyzes it to determine its nature and intent.
3.  **Agent Transfer:** Based on its evaluation, the `root_agent` transfers control of the conversation to the most relevant specialized agent (e.g., `summarizer`, `qa_agent`, `support_router`, `classifier`).
4.  **Specialized Agent Response:** The designated agent processes the query and provides the appropriate response or action. If the specialized agent determines another agent is better suited, it can transfer control further.

This architecture ensures a streamlined and effective handling of diverse user requests, leveraging the specific capabilities of each AI agent.
