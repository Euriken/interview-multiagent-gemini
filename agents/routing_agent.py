# Multi-agent Router (sequential workflow)

class InterviewRouter:
    def __init__(self, hr, tech, beh):
        self.hr = hr
        self.tech = tech
        self.beh = beh

    def run_full_interview(self, role="Software Engineer"):
        return {
            "hr_question": self.hr.ask_question(role),
            "technical_question": self.tech.ask_question(role),
            "behavioral_question": self.beh.ask_question()
        }
