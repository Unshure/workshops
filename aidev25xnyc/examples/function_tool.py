from strands import Agent, tool

@tool
def multiply(x: int, y: int) -> int:
    print(f"\tMultiplying {x}*{y}")
    result = x * y
    print(f"\tResult: {result}")
    return result

agent = Agent(
    tools=[multiply],
)

agent("What is 123 * 456")
