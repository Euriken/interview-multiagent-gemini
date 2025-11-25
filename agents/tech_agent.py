# Technical Interview Agent

from google import genai

class TechnicalInterviewer:
    def __init__(self, client, company="Google"):
        self.client = client
        self.company = company

    def ask_question(self, role):
        prompt = f"""
        You are a technical interviewer at {self.company}.
        Ask ONE interview question for a {role} role.
        Only high-quality questions.
        """
        resp = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return resp.text
