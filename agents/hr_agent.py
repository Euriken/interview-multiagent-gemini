# HR Interview Agent (Gemini-powered)

from google import genai

class HRInterviewer:
    def __init__(self, client):
        self.client = client

    def ask_question(self, role):
        prompt = f"""
        You are an HR interviewer for a {role} interview.
        Ask one HR screening question. Keep it short.
        """
        resp = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return resp.text
