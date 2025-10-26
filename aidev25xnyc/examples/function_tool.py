from strands import Agent, tool

@tool
def multiply(x: int, y: int) -> int:
    return x * y

agent = Agent(
    tools=[multiply],
)

agent("What is 123 * 456")
