from .llm import MockLLM
from .session import Session

def run_once(user_input: str) -> str:
    session = Session()
    session.add_user(user_input)
    reply = MockLLM().chat(session.messages)
    session.add_assistant(reply)
    return reply
