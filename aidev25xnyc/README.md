# AI Dev 25 X NYC

A collection of examples demonstrating AI agent capabilities using the Strands framework.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Model Credentials**
  Setup [AWS Credentials for Bedrock access](https://strandsagents.com/latest/documentation/docs/user-guide/quickstart/#configuring-credentials) in order to run examples.

3. **Set environment variables:**
   ```bash
   export OPENAI_API_KEY="your-openai-key"  # For OpenAI examples
   export TAVILY_API_KEY="your-tavily-key"  # For tavily tool examples
   export STRANDS_TOOL_CONSOLE_MODE="enabled"  # For enhanced strands tool output

   ```

## Examples

- **`first_strands.py`** - Basic agent with calculator tool and pirate personality
- **`openai_strands.py`** - Same agent using OpenAI GPT-4 model
- **`function_tool.py`** - Simple custom tool example
- **`swarm.py`** - Multi-agent system with web research, file editing, and shell capabilities
- **`agent_as_tool.py`** - Demonstrates wrapping agents as reusable tools
- **`meta_agent.py`** - Agent that can use other agents as tools

## Quick Start

Run any example:
```bash
python -u first_strands.py
```

Most examples include interactive loops - type your queries and press Enter to interact with the agents.
