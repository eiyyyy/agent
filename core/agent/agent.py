from ..llm.mock_llm import MockLLM
from ..session.session import Session


class Agent:
    def __init__(self):
        self.llm = MockLLM()
        self.session = Session()

    def run(self, user_input: str) -> str:
        self.session.add_user(user_input)
        reply = self.llm.chat(self.session.messages)
        self.session.add_assistant(reply)
        return reply
