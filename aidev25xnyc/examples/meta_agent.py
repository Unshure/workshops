from strands import Agent
from strands_tools import use_agent, editor, shell

agent = Agent(
    system_prompt="You MUST use the `use_agent` tool write or run files.",
    tools=[use_agent, editor, shell]
)

agent("Write a python script to print a christmas tree, then execute it")

while True:
    _ = agent(input("\nInput: "))