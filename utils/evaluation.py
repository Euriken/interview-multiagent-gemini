# Interview answer evaluator

from google import genai

class Evaluator:
    def __init__(self, client):
        self.client = client

    def evaluate(self, question, answer):
        prompt = f"""
        Evaluate this interview answer.

        QUESTION: {question}
        ANSWER: {answer}

        Return a JSON:
        {{
           "score": 1-10,
           "feedback": "clear explanation"
        }}
        """

        resp = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return resp.text
