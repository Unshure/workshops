from strands import Agent
from strands.multiagent import Swarm
from strands_tools import tavily, file_read, file_write, shell

web_researcher_agent = Agent(
    name="web",
    system_prompt=
    "You research a query and give a one sentence summary",
    tools=[tavily]
)

file_editor_agent = Agent(
    name="file",
    system_prompt="write files",
    tools=[file_read, file_write]
)

shell_agent = Agent(
    name="shell",
    system_prompt="You interact with shell",
    tools=[shell]
)

swarm = Swarm([
    web_researcher_agent,
    file_editor_agent,
    shell_agent
])

swarm(
  "Research pine trees, write a python script " \
  "to print the summary, then execute it"
)