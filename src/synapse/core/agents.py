import asyncio

class Agent:
    def __init__(self, name):
        self.name = name

    async def run_task(self, task_func, *args):
        """Run a task asynchronously"""
        result = await asyncio.to_thread(task_func, *args)
        return result

async def run_parallel_agents(agents, task_func, *args):
    """Run tasks in parallel for multiple agents"""
    tasks = [agent.run_task(task_func, agent.name, *args) for agent in agents]
    results = await asyncio.gather(*tasks)
    return results

def sample_task(agent_name, data):
    """Sample task: process data"""
    return f"{agent_name} processed {data}"

async def test_parallel():
    agents = [Agent("Alice"), Agent("Bob")]
    results = await run_parallel_agents(agents, sample_task, "data")
    return results

if __name__ == "__main__":
    results = asyncio.run(test_parallel())
    print("Parallel results:", results)
