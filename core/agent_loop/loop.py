from ..agent.agent import Agent


def run_once(user_input: str) -> str:
    return Agent().run(user_input)
