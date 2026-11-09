from core.agent_loop import run_once
from core.session import Session

def test_run_once_returns_string():
    out = run_once("hello")
    assert isinstance(out, str)
    assert len(out) > 0

def test_session_records_messages():
    s = Session()
    s.add_user("hi")
    s.add_assistant("hey")
    assert len(s.messages) == 3
    assert s.messages[1]["content"] == "hi"

if __name__ == "__main__":
    test_run_once_returns_string()
    test_session_records_messages()
    print("All tests passed.")
