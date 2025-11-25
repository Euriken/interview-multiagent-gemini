
# **Interview Multi-Agent Gemini**

A multi-agent AI interview simulator built using Google Gemini and LangGraph.
The system includes HR, Technical, and Behavioral interviewer agents, each equipped with company-specific question profiles (Google, Meta, Amazon).
It supports sequential multi-agent workflows, memory, company-aware evaluation, and generates structured interview feedback reports.

This project is developed as part of the **Google x Kaggle AI Agents Intensive Capstone (Nov 2025)**.

---

## **1. Project Overview**

Modern interview preparation is fragmented, generic, and does not adapt to different companies or roles.
This project provides an intelligent, multi-agent approach to simulate real interview pipelines, giving users role-specific, company-specific guidance automatically.

The solution uses a chain of AI agents:

1. **Routing Agent**
   Determines which interviewer agent should respond next based on conversation state.

2. **HR Agent**
   Screens for soft skills, communication clarity, stability of intent, and general professional fit.

3. **Technical Agent**
   Conducts technical Q&A. For software roles, it evaluates algorithmic reasoning, systems thinking, and debugging ability.

4. **Behavioral Agent**
   Uses STAR-method evaluation. Asks targeted leadership, conflict-resolution, and ownership-oriented questions.

5. **Evaluation Engine**
   Generates a structured final report summarizing performance across all interview dimensions.

---

## **2. Features**

### **Multi-Agent Architecture**

* Sequential workflow built with LangGraph.
* Routing agent decides flow: HR → Technical → Behavioral → Evaluation.
* Each agent has its own prompt, memory, and scoring rubric.

### **Company-Specific Question Banks**

Supports specialized interview styles for:

* Google
* Meta
* Amazon

Each profile includes:

* Technical question style
* Behavioral leadership principles
* Difficulty scaling
* Evaluation rubrics

### **Session Memory**

* Each agent retains context using LangGraph memory nodes.
* Conversation state is carried across interview rounds.

### **Structured Evaluation Reports**

The Evaluation Engine produces:

* Strengths
* Weaknesses
* Category-wise scores
* A final hiring recommendation
* Improvement suggestions
* Company-adjusted scoring dimensions

### **Configurable Runtime**

Users can:

* Choose company
* Choose role
* Select difficulty
* Run a complete simulated interview session

---

## **3. Repository Structure**

```
.
├── agents/
│   ├── hr_agent.py
│   ├── technical_agent.py
│   ├── behavioral_agent.py
│   └── routing_agent.py
│
├── utils/
│   ├── questions_google.json
│   ├── questions_meta.json
│   ├── questions_amazon.json
│   └── evaluation.py
│
├── main.py
├── run_demo.py
├── LICENSE
└── README.md
```

---

## **4. How It Works**

### **1. User selects:**

* Target company (Google, Meta, Amazon)
* Role (Engineering, Analyst, General)
* Difficulty level

### **2. System initializes the agent workflow**

* Routing agent creates the interview path
* Memory is prepared
* Question sets are loaded

### **3. Interview progresses through agents**

Example sequence:

* HR agent asks screening questions
* Technical agent evaluates reasoning
* Behavioral agent checks leadership and culture fit

### **4. Evaluation Engine generates a complete report**

Includes:

* Company-specific competency mapping
* STAR-based behavioral grading
* Technical depth analysis
* Hiring recommendation

---

## **5. Requirements**

* Python 3.10+
* Google Gemini API Key
* Following packages:

  * google-genai
  * langgraph
  * langchain
  * pydantic
  * jinja2

---

## **6. Running the Project**

### **1. Set your Gemini API key**

```
export GOOGLE_API_KEY="your_key_here"
```

### **2. Run the demo**

```
python run_demo.py
```

### **3. Or run the full workflow**

```
python main.py
```

---

## **7. Capstone Requirements Mapping**

| Requirement                   | Included                                        |
| ----------------------------- | ----------------------------------------------- |
| Multi-agent system            | Yes (HR, Technical, Behavioral, Routing)        |
| Sequential or parallel agents | Sequential workflow implemented                 |
| Memory / state management     | LangGraph memory used                           |
| Tools                         | Custom evaluation tool + structured report tool |
| Context engineering           | Custom prompting + company-specific context     |
| Observability                 | Modular architecture with logs                  |
| Evaluation                    | Automatic scoring and final report              |

---

## **8. License**

Released under the **MIT License**.

---

## **9. Acknowledgements**

This project was created as part of the **Google AI Agents Intensive x Kaggle Capstone Program (2025)**.

---
