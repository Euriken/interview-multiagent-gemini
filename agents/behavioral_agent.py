# Behavioral Interview Agent

class BehavioralInterviewer:
    def __init__(self, client):
        self.client = client

    def ask_question(self):
        prompt = """
        Ask one STAR-method behavioral interview question.
        Keep it concise.
        """
        resp = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return resp.text
