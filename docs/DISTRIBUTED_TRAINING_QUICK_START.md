# Distributed Agent Training - Quick Start Guide

## Installation

### Basic Setup
```bash
pip install numpy
```

### For MPI Support
```bash
# macOS
brew install open-mpi
pip install mpi4py

# Linux (Ubuntu/Debian)
sudo apt-get install libopenmpi-dev
pip install mpi4py
```

### For Spark Support
```bash
pip install pyspark
```

## 5-Minute Quick Start

### 1. Local Training (Single Machine)

```python
import asyncio
import numpy as np
from synapse.core.distributed_training import (
    DistributedTrainer,
    simple_loss_function
)

async def main():
    # Create trainer with 5 agents
    trainer = DistributedTrainer([
        "agent1", "agent2", "agent3", "agent4", "agent5"
    ])
    
    # Initialize weights
    trainer.initialize_weights(np.array([1.0, 1.0]))
    
    # Train
    results = await trainer.train(
        loss_fn=simple_loss_function,
        iterations=50,
        learning_rate=0.05,
        sync_interval=5
    )
    
    # Print results
    print(f"Training complete in {results['total_time']:.2f}s")
    for agent_id, result in results['agent_results'].items():
        print(f"{agent_id}: loss={result['final_loss']:.6f}")

asyncio.run(main())
```

### 2. Using the CLI Tool

```bash
# Basic training
synapse train --agents=5 --iterations=50 --backend=local

# With output
synapse train \
  --agents=10 \
  --iterations=100 \
  --learning-rate=0.05 \
  --output=results.json \
  --verbose

# With different loss function
synapse train \
  --agents=20 \
  --loss-function=ackley \
  --sync-interval=5 \
  --backend=local
```

### 3. MPI Training (HPC Clusters)

```python
# train_mpi.py
import asyncio
import numpy as np
from synapse.core.distributed_training import (
    MPIDistributedTrainer,
    ackley_loss_function
)

async def main():
    agents = [f"agent{i}" for i in range(100)]
    trainer = MPIDistributedTrainer(agents)
    
    trainer.initialize_weights(np.array([0.5, 0.5]))
    
    results = await trainer.train(
        loss_fn=ackley_loss_function,
        iterations=100,
        learning_rate=0.01,
        sync_interval=10
    )
    
    # Only rank 0 prints
    if trainer.rank == 0:
        print(f"Distributed training complete!")

asyncio.run(main())
```

```bash
# Run with MPI
mpirun -n 4 python train_mpi.py
```

### 4. Spark Training (Distributed Computing)

```python
# train_spark.py
import asyncio
import numpy as np
from synapse.core.distributed_training import (
    SparkDistributedTrainer,
    simple_loss_function
)

async def main():
    agents = [f"agent{i}" for i in range(1000)]
    
    trainer = SparkDistributedTrainer(
        agents,
        spark_master="spark://master:7077"  # or "local[*]"
    )
    
    trainer.initialize_weights(np.array([1.0, 1.0, 1.0]))
    
    results = await trainer.train(
        loss_fn=simple_loss_function,
        iterations=100,
        learning_rate=0.05,
        sync_interval=5
    )
    
    print("Training complete!")
    trainer.stop()

asyncio.run(main())
```

### 5. Custom Loss Function

```python
from typing import Tuple
import numpy as np

def my_loss_function(weights: np.ndarray) -> Tuple[float, np.ndarray]:
    """
    Custom loss function.
    
    Args:
        weights: Input weights
        
    Returns:
        (loss, gradients) tuple
    """
    # Your loss computation
    loss = np.sum(weights ** 3)  # Example: cubic loss
    
    # Your gradient computation
    gradients = 3 * weights ** 2
    
    return float(loss), gradients

# Use it
trainer = DistributedTrainer(["a1", "a2", "a3"])
results = await trainer.train(
    loss_fn=my_loss_function,
    iterations=50,
    learning_rate=0.05
)
```

## Common Patterns

### Pattern 1: Multi-Agent Convergence

```python
async def train_to_convergence(max_iterations=1000):
    trainer = DistributedTrainer([f"agent{i}" for i in range(10)])
    trainer.initialize_weights(np.random.randn(5))
    
    for epoch in range(10):
        results = await trainer.train(
            loss_fn=simple_loss_function,
            iterations=100,
            learning_rate=0.05 * (0.9 ** epoch),  # Decay learning rate
            sync_interval=10
        )
        
        avg_loss = np.mean([
            r['final_loss']
            for r in results['agent_results'].values()
        ])
        
        print(f"Epoch {epoch}: avg_loss={avg_loss:.6f}")
        
        if avg_loss < 0.0001:
            print("Converged!")
            break
```

### Pattern 2: Sync Interval Tuning

```python
async def find_optimal_sync_interval(loss_fn, max_sync=50):
    results_by_interval = {}
    
    for sync_interval in [1, 5, 10, 20, 50]:
        trainer = DistributedTrainer([f"a{i}" for i in range(20)])
        trainer.initialize_weights(np.array([1.0, 1.0]))
        
        results = await trainer.train(
            loss_fn=loss_fn,
            iterations=100,
            learning_rate=0.05,
            sync_interval=sync_interval
        )
        
        results_by_interval[sync_interval] = results['total_time']
    
    best = min(results_by_interval, key=results_by_interval.get)
    print(f"Optimal sync interval: {best}")
    return best
```

### Pattern 3: Agent Inspection

```python
async def inspect_agent_states(trainer):
    results = await trainer.train(
        loss_fn=simple_loss_function,
        iterations=50,
        learning_rate=0.05,
        sync_interval=10
    )
    
    # Get individual agents
    for agent_id in ["agent1", "agent2"]:
        agent = trainer.get_agent(agent_id)
        
        print(f"\n{agent_id}:")
        print(f"  Weights: {agent.state.weights}")
        print(f"  Loss: {agent.state.loss:.6f}")
        print(f"  Iterations: {agent.state.iteration}")
        print(f"  Syncs: {len(agent.learning_history)}")
```

## Troubleshooting

### Issue: Tests Timeout
**Solution:** Run individual tests instead of full suite:
```bash
pytest tests/test_phase16_3_distributed_training.py::TestDistributedAgent -v
```

### Issue: MPI Import Error
**Solution:** Install mpi4py correctly:
```bash
# Ensure OpenMPI/MPICH is installed first
which mpirun

# Then install mpi4py
pip install mpi4py --force-reinstall
```

### Issue: Spark Memory Error
**Solution:** Increase Spark memory:
```bash
export SPARK_WORKER_MEMORY=4g
export SPARK_DRIVER_MEMORY=2g
spark-submit your_script.py
```

### Issue: Slow Synchronization
**Solution:** Tune sync interval:
```python
# Increase interval to sync less often
results = await trainer.train(
    loss_fn=loss_fn,
    iterations=1000,
    learning_rate=0.05,
    sync_interval=50  # Sync every 50 iterations instead of 10
)
```

### Issue: Non-Convergent Training
**Solution:** Adjust learning rate and loss function:
```python
# Reduce learning rate
results = await trainer.train(
    loss_fn=loss_fn,
    learning_rate=0.01,  # Lower rate
    sync_interval=5
)

# Or use different loss function
from synapse.core.distributed_training import ackley_loss_function
results = await trainer.train(
    loss_fn=ackley_loss_function,  # Try different function
    learning_rate=0.05,
    sync_interval=5
)
```

## API Cheat Sheet

### DistributedTrainer Methods

```python
# Create trainer
trainer = DistributedTrainer(agent_ids: List[str])

# Initialize weights
trainer.initialize_weights(weights: np.ndarray)

# Train
results = await trainer.train(
    loss_fn: Callable,
    iterations: int,
    learning_rate: float,
    sync_interval: int
)

# Get agent
agent = trainer.get_agent(agent_id: str)

# Get summary
summary = trainer.get_summary()
```

### DistributedAgent Methods

```python
agent = trainer.get_agent("agent1")

# Training step
loss = await agent.train_step(loss_fn, learning_rate)

# Synchronization
await agent.synchronize()

# Barrier
await agent.barrier_sync()

# State access
state = agent.get_state()
agent.set_weights(weights)
```

### Loss Function Signature

```python
def my_loss_fn(weights: np.ndarray) -> Tuple[float, np.ndarray]:
    """
    Args:
        weights: numpy array of weights
        
    Returns:
        (loss: float, gradients: np.ndarray)
    """
    loss = compute_loss(weights)
    gradients = compute_gradients(weights)
    return loss, gradients
```

## Performance Tips

1. **Batch Processing**: Use larger `sync_interval` for fewer syncs
2. **Learning Rate**: Start high, decay over time: `lr * (0.9 ** epoch)`
3. **Agents**: More agents = better convergence, more sync overhead
4. **Loss Function**: Keep it fast; avoid heavy computation
5. **Network**: Use MPI for low-latency networks, Spark for cloud

## Useful Resources

- [Full Documentation](PHASE_16_3_DISTRIBUTED_TRAINING.md)
- [Phase 16.3 Summary](PHASE_16_3_SUMMARY.md)
- [Architecture Overview](#architecture-overview)

## Next Steps

- Integrate with Phase 16.1 (LLM Code Generation)
- Use with synapse-agents stdlib
- Add custom synchronization strategies
- Implement gradient compression
- Add fault tolerance

---

Happy distributed training! 🚀
