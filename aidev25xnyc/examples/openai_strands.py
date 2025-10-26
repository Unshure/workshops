import os
from strands import Agent
from strands.models.openai import OpenAIModel
from strands_tools import calculator

openai_model = OpenAIModel(
    model_id="gpt-4",
    client_args={
        "api_key": os.environ.get("OPENAI_API_KEY")
    }
)

agent = Agent(
    model=openai_model,
    tools=[calculator],
    system_prompt="You are a helpful assistant."
)

agent("What is the sqrt of 1764?")

while True:
    _ = agent(input("\nInput: "))