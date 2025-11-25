# Simple memory system

class MemoryBank:
    def __init__(self):
        self.history = []

    def store(self, question, answer):
        self.history.append({"q": question, "a": answer})

    def get(self):
        return self.history
