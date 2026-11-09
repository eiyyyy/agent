class Session:
    """最小会话：存消息列表。"""

    def __init__(self):
        self.messages: list[dict] = [
            {"role": "system", "content": "你是 dsh 最小 core demo"}
        ]

    def add_user(self, text: str):
        self.messages.append({"role": "user", "content": text})

    def add_assistant(self, text: str):
        self.messages.append({"role": "assistant", "content": text})
