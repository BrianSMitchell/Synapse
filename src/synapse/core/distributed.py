import asyncio
from synapse.core.agents import Agent, run_parallel_agents

# Simple shared state
shared_state = {}

def update_shared(agent_name, key, value):
    """Update shared state"""
    shared_state[key] = value
    return f"{agent_name} updated {key} to {value}"

def read_shared(agent_name, key):
    """Read from shared state"""
    value = shared_state.get(key, None)
    return f"{agent_name} read {key}: {value}"

async def test_distributed():
    agents = [Agent("Alice"), Agent("Bob")]
    # Update
    await run_parallel_agents(agents[:1], update_shared, "global_var", 42)
    # Read
    results = await run_parallel_agents(agents, read_shared, "global_var")
    consistent = all("42" in r for r in results)
    return consistent

if __name__ == "__main__":
    result = asyncio.run(test_distributed())
    print("Consistent global state:", result)
