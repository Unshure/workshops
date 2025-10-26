from strands import Agent
from strands_tools import calculator

agent = Agent(
    model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
    tools=[calculator],
    system_prompt="You are a helpful assistant!"
)

agent("What is the sqrt of 1764?")

while True:
    _ = agent(input("\nInput: "))