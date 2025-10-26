from strands import Agent, tool
from strands_tools import tavily
import json

web_researcher_agent = Agent(
    system_prompt="You research a query and give a one sentence summary",
    tools=[tavily]
)

@tool
def web_researcher(query: str) -> str:
    summary = str(web_researcher_agent(query))
    return summary

agent = Agent(
    tools=[web_researcher],
)

agent("Tell me about Andrew Ng, or explain any errors your face")


print(f"\n\nMain Agent context: {len(json.dumps(agent.messages))}")
print(f"Web Agent context:  {len(json.dumps(web_researcher_agent.messages))}")

while True:
    _ = agent(input("\nInput: "))