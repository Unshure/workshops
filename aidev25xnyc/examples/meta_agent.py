import logging
from strands import Agent
from strands_tools import use_agent, file_read, file_write, shell

# Enables Strands debug log level
logging.getLogger("strands_tools.use_agent").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

agent = Agent(
    system_prompt=
    "You MUST use the `use_agent` tool write or run files.",
    tools=[use_agent, file_read, file_write, shell]
)

agent(
    "Write a script to print a christmas tree, then run it"
)

while True:
    _ = agent(input("\nInput: "))

