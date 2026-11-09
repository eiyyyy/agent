class MockLLM:
    """最小 LLM 封装：不真调 API，直接回一句固定话。"""

    def chat(self, messages: list[dict]) -> str:
        last = messages[-1]
        return f"[mock-llm] 收到: {last['content']}"
