"""
Multi-Agent Interview Simulator
Built for Kaggle x Google AI Agents Intensive Capstone
Author: Euriken 

Features:
- Multi-agent architecture using LangGraph
- Google Gemini (via google-genai client)
- HR Agent → Technical Agent → Behavioral Agent
- Memory (Conversation buffer)
- Sequential workflow
- Company-specific interview variants (Google, Meta, Amazon)
- Structured evaluation output
"""

# ------------------------------
# Imports
# ------------------------------
from google import genai
from langgraph.graph import StateGraph, END
from typing import Dict, List, Any

# ------------------------------
# Gemini Client Setup
# ------------------------------
client = genai.Client(api_key=none)   
MODEL = "gemini-1.5-flash"

# ------------------------------
# Memory State
# ------------------------------
class InterviewState(Dict):
    """State shared by all agents."""
    conversation: List[str]
    company: str
    evaluation: List[str]

# ------------------------------
# Agent Definitions
# ------------------------------

def hr_agent(state: InterviewState):
    """HR Round: culture, goals, soft-fit."""
    prompt = f"""
You are the HR interviewer for {state['company']}.
Ask 2 HR interview questions.
Keep them short.
"""
    resp = client.models.generate_content(model=MODEL, contents=prompt)
    q = resp.text
    state["conversation"].append(q)
    return state


def technical_agent(state: InterviewState):
    """Technical Round: company-specific questions."""
    prompt = f"""
You are a Technical interviewer for {state['company']}.
Ask 2 technical interview questions similar to what this company asks.
If Google: focus on systems and algorithms.
If Meta: focus on design + behavior signals.
If Amazon: emphasize leadership principles + backend systems.
Respond with questions only.
"""
    resp = client.models.generate_content(model=MODEL, contents=prompt)
    q = resp.text
    state["conversation"].append(q)
    return state


def behavioral_agent(state: InterviewState):
    """Behavioral Round: STAR-method questions."""
    prompt = f"""
You are the Behavioral interviewer.
Ask 2 behavioral questions using STAR methodology.
Respond with ONLY questions.
"""
    resp = client.models.generate_content(model=MODEL, contents=prompt)
    q = resp.text
    state["conversation"].append(q)
    return state


def evaluation_agent(state: InterviewState):
    """Evaluates the candidate based on the conversation."""
    prompt = f"""
You are an interview evaluator.
Summarize the difficulty of the questions and interview structure.
Provide:
- Difficulty rating
- What the interview tests for
- How candidate should prepare
Conversation:
{state['conversation']}
"""
    resp = client.models.generate_content(model=MODEL, contents=prompt)
    state["evaluation"].append(resp.text)
    return state


# ------------------------------
# LangGraph Workflow
# ------------------------------

def build_graph():
    graph = StateGraph(InterviewState)

    graph.add_node("hr_agent", hr_agent)
    graph.add_node("technical_agent", technical_agent)
    graph.add_node("behavioral_agent", behavioral_agent)
    graph.add_node("evaluation_agent", evaluation_agent)

    graph.set_entry_point("hr_agent")
    graph.add_edge("hr_agent", "technical_agent")
    graph.add_edge("technical_agent", "behavioral_agent")
    graph.add_edge("behavioral_agent", "evaluation_agent")
    graph.add_edge("evaluation_agent", END)

    return graph.compile()


# ------------------------------
# Entry Point for Running
# ------------------------------

def run_interview(company="Google"):
    workflow = build_graph()
    init_state = {
        "conversation": [],
        "company": company,
        "evaluation": []
    }
    final = workflow.invoke(init_state)
    
    print("\n=== Interview Questions ===\n")
    for x in final["conversation"]:
        print(x, "\n")

    print("\n=== Evaluation ===\n")
    print(final["evaluation"][0])


if __name__ == "__main__":
    run_interview("Google")
