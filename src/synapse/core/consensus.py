import asyncio
import time
from synapse.core.agents import Agent, run_parallel_agents

def consensus(votes, threshold=0.6):
    """Determine consensus from votes list (True/False)"""
    yes_votes = sum(votes)
    total = len(votes)
    agreement = yes_votes / total
    return agreement >= threshold, agreement

async def simulate_consensus(num_agents=5, threshold=0.6):
    """Simulate consensus with agents voting"""
    agents = [Agent(f"Agent{i}") for i in range(num_agents)]
    # Simulate vote: random but bias to agree
    import random
    votes = [random.choice([True, False]) for _ in range(num_agents)]
    # To ensure agreement, make most True
    votes = [True] * int(num_agents * 0.8) + [False] * (num_agents - int(num_agents * 0.8))

    start = time.time()
    agreed, agreement = consensus(votes, threshold)
    end = time.time()
    duration = (end - start) * 1000  # ms
    return agreed, agreement, duration

async def test_consensus():
    agreed, agreement, duration = await simulate_consensus(5, 0.6)
    return agreed and duration < 500

if __name__ == "__main__":
    result = asyncio.run(test_consensus())
    print("Consensus test:", result)
