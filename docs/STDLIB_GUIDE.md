# Synapse Standard Library Guide

**Version:** 1.0  
**Date:** November 16, 2025  
**Status:** Phase 15.2 - Complete  

---

## Overview

The Synapse Standard Library provides three main modules for common programming tasks:

1. **synapse-math**: Numerical computing and array operations
2. **synapse-agents**: Multi-agent systems and coordination
3. **synapse-ml**: Machine learning helpers and model training

Each module is implemented in pure Synapse and can be imported using:

```synapse
import "stdlib/math.syn"
import "stdlib/agents.syn"
import "stdlib/ml.syn"
```

---

## Module 1: synapse-math

### Overview

NumPy-like array operations for scientific computing in Synapse.

### Array Creation

#### `zeros(n)` → array
Create an array of n zeros.
```synapse
let z = zeros(5)  // [0, 0, 0, 0, 0]
```

#### `ones(n)` → array
Create an array of n ones.
```synapse
let o = ones(3)  // [1, 1, 1]
```

#### `arange(start, end, step)` → array
Create array from start to end (exclusive) with given step.
```synapse
let r = arange(0, 5, 1)  // [0, 1, 2, 3, 4]
let r = arange(0, 1, 0.25)  // [0, 0.25, 0.5, 0.75]
```

#### `linspace(start, end, count)` → array
Create array with count evenly spaced values from start to end.
```synapse
let ls = linspace(0, 1, 5)  // [0, 0.25, 0.5, 0.75, 1]
```

#### `eye(n)` → matrix
Create n×n identity matrix.
```synapse
let i = eye(3)
// [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

### Array Operations

#### `shape(arr)` → array
Get dimensions of array. Returns [size] for 1D, [rows, cols] for 2D.
```synapse
let s = shape([1, 2, 3])  // [3]
let s = shape([[1, 2], [3, 4]])  // [2, 2]
```

#### `flatten(matrix)` → array
Flatten 2D array to 1D.
```synapse
let f = flatten([[1, 2], [3, 4]])  // [1, 2, 3, 4]
```

#### `reshape(arr, dims)` → matrix
Reshape 1D array to 2D with given dimensions.
```synapse
let r = reshape([1, 2, 3, 4, 5, 6], [2, 3])
// [[1, 2, 3], [4, 5, 6]]
```

#### `transpose(matrix)` → matrix
Transpose 2D array (swap rows and columns).
```synapse
let t = transpose([[1, 2], [3, 4]])  // [[1, 3], [2, 4]]
```

### Aggregation Functions

#### `sum(arr)` → number
Sum all elements.
```synapse
let s = sum([1, 2, 3, 4, 5])  // 15
```

#### `mean(arr)` → number
Calculate average.
```synapse
let m = mean([1, 2, 3, 4, 5])  // 3
```

#### `min(arr)` → number
Find minimum value.
```synapse
let mn = min([5, 2, 8, 1, 9])  // 1
```

#### `max(arr)` → number
Find maximum value.
```synapse
let mx = max([5, 2, 8, 1, 9])  // 9
```

#### `std(arr)` → number
Calculate standard deviation.
```synapse
let s = std([1, 2, 3, 4, 5])  // Sample std dev
```

### Element-wise Operations

#### `add(arr1, arr2)` → array
Element-wise addition.
```synapse
let sum = add([1, 2, 3], [4, 5, 6])  // [5, 7, 9]
```

#### `multiply(arr1, arr2)` → array
Element-wise multiplication.
```synapse
let prod = multiply([1, 2, 3], [2, 2, 2])  // [2, 4, 6]
```

#### `scale(arr, factor)` → array
Multiply all elements by scalar.
```synapse
let scaled = scale([1, 2, 3], 2)  // [2, 4, 6]
```

### Linear Algebra

#### `dot(vec1, vec2)` → number
Dot product of two vectors.
```synapse
let d = dot([1, 2, 3], [4, 5, 6])  // 32
```

#### `matmul(mat1, mat2)` → matrix
Matrix multiplication.
```synapse
let m = matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
// [[19, 22], [43, 50]]
```

#### `norm(vec)` → number
Euclidean norm (length) of vector.
```synapse
let n = norm([3, 4])  // 25 (not sqrt, raw sum of squares)
```

### Utilities

#### `append(arr, value)` → array
Add element to end of array.
```synapse
let a = append([1, 2, 3], 4)  // [1, 2, 3, 4]
```

#### `reverse(arr)` → array
Reverse array.
```synapse
let r = reverse([1, 2, 3])  // [3, 2, 1]
```

#### `clip(arr, min, max)` → array
Clip values to [min, max] range.
```synapse
let c = clip([-5, 0, 5, 10], 0, 5)  // [0, 0, 5, 5]
```

---

## Module 2: synapse-agents

### Overview

Framework for building multi-agent systems with task coordination and consensus.

### Agent Creation

#### `create_agent(id, name, capacity)` → agent
Create a new agent.
```synapse
let agent = create_agent(1, "alice", 10)
```

#### `create_agent_pool(count)` → array[agent]
Create pool of agents.
```synapse
let pool = create_agent_pool(5)
```

### Agent Properties

#### `agent_get(agent, key)` → value
Get agent property.
```synapse
let name = agent_get(agent, "name")
let cap = agent_get(agent, "capacity")
```

#### `agent_set(agent, key, value)` → agent
Set agent property.
```synapse
let updated = agent_set(agent, "name", "bob")
```

### Task Management

#### `submit_task(agent, task_id, task_data)` → agent
Submit task to agent.
```synapse
let agent = submit_task(agent, 1, "compute_sum")
```

#### `get_pending_tasks(agent)` → array
Get all pending tasks.
```synapse
let tasks = get_pending_tasks(agent)
```

#### `complete_task(agent, task_id)` → agent
Mark task as completed.
```synapse
let agent = complete_task(agent, 1)
```

#### `has_capacity(agent)` → bool
Check if agent can accept more tasks.
```synapse
if has_capacity(agent) {
    agent = submit_task(agent, 2, "new_task")
}
```

#### `agent_load(agent)` → number
Get current task count of agent.
```synapse
let load = agent_load(agent)
```

### Task Scheduling

#### `distribute_task(agents, task_id, task_data)` → bool
Distribute task to agent with available capacity.
```synapse
let success = distribute_task(pool, 5, "task_data")
```

#### `find_available_agent(agents)` → agent
Find first agent with capacity.
```synapse
let agent = find_available_agent(pool)
```

#### `balance_tasks(agents)` → array[agent]
Simple load balancing.
```synapse
let balanced = balance_tasks(pool)
```

### Consensus

#### `consensus_majority(votes)` → value
Determine consensus via majority vote.
```synapse
let consensus = consensus_majority([1, 1, 0, 1, 0])  // 1
```

#### `consensus_weighted(votes, weights)` → value
Determine consensus via weighted voting.
```synapse
let votes = [1, 0, 1]
let weights = [0.5, 0.3, 0.2]
let consensus = consensus_weighted(votes, weights)
```

### Communication

#### `create_message(sender_id, receiver_id, content)` → message
Create message between agents.
```synapse
let msg = create_message(1, 2, "hello")
```

#### `send_message(agents, message)` → bool
Send message from one agent to another.
```synapse
let success = send_message(pool, msg)
```

### State Management

#### `agent_state_set(agent, key, value)` → agent
Set agent state variable.
```synapse
let agent = agent_state_set(agent, "energy", 100)
```

#### `agent_state_get(agent, key)` → value
Get agent state variable.
```synapse
let energy = agent_state_get(agent, "energy")
```

---

## Module 3: synapse-ml

### Overview

Machine learning helpers for model creation, training, and evaluation.

### Model Management

#### `create_model(type, input_dim, output_dim)` → model
Create ML model.
```synapse
let model = create_model("linear", 5, 1)
let model = create_model("logistic", 10, 1)
```

#### `model_get(model, key)` → value
Get model property.
```synapse
let mtype = model_get(model, "type")
let lr = model_get(model, "lr")
```

#### `model_set(model, key, value)` → model
Set model property.
```synapse
let model = model_set(model, "lr", 0.001)
```

#### `init_weights(model)` → model
Initialize model weights randomly.
```synapse
let model = init_weights(model)
```

### Activation Functions

#### `sigmoid(x)` → number
Sigmoid activation: 1 / (1 + e^-x)
```synapse
let s = sigmoid(0)  // ~0.5
let s = sigmoid(10)  // ~1.0
```

#### `relu(x)` → number
ReLU activation: max(0, x)
```synapse
let r = relu(5)   // 5
let r = relu(-5)  // 0
```

#### `tanh_approx(x)` → number
Tanh approximation for stability.
```synapse
let t = tanh_approx(0)  // ~0
```

#### `softmax(logits)` → array
Softmax for multi-class probability distribution.
```synapse
let probs = softmax([1, 2, 3])
// [~0.09, ~0.24, ~0.67]
```

### Loss Functions

#### `linear_mse_loss(y_true, y_pred)` → number
Mean Squared Error for regression.
```synapse
let loss = linear_mse_loss([1, 2, 3], [1.1, 1.9, 3.2])
```

#### `logistic_loss(y_true, y_pred)` → number
Binary cross-entropy for classification.
```synapse
let loss = logistic_loss([1, 0, 1], [0.9, 0.1, 0.8])
```

### Prediction

#### `linear_predict(model, x)` → number
Linear regression prediction.
```synapse
let pred = linear_predict(model, [1, 2, 3, 4, 5])
```

#### `logistic_predict(model, x)` → number
Binary classification prediction (0-1 probability).
```synapse
let prob = logistic_predict(model, [1, 2, 3, 4, 5])
```

### Evaluation Metrics

#### `accuracy(y_true, y_pred)` → number
Classification accuracy (0-1).
```synapse
let acc = accuracy([1, 0, 1, 1], [0.9, 0.2, 0.8, 0.7])
```

#### `precision(y_true, y_pred)` → number
Precision metric: TP / (TP + FP)
```synapse
let prec = precision([1, 1, 0, 0], [0.9, 0.8, 0.3, 0.4])
```

#### `recall(y_true, y_pred)` → number
Recall metric: TP / (TP + FN)
```synapse
let rec = recall([1, 1, 0, 0], [0.9, 0.2, 0.3, 0.4])
```

#### `f1_score(y_true, y_pred)` → number
F1 Score: 2 * (precision * recall) / (precision + recall)
```synapse
let f1 = f1_score([1, 1, 0, 0], [0.9, 0.8, 0.3, 0.4])
```

### Training

#### `gradient_descent_step(model, x_batch, y_batch, loss_fn)` → model
Single gradient descent step.
```synapse
let model = gradient_descent_step(model, x_train, y_train, linear_mse_loss)
```

### Data Processing

#### `create_batches(data, batch_size)` → array[array]
Split data into batches.
```synapse
let batches = create_batches([1, 2, 3, 4, 5], 2)
// [[1, 2], [3, 4], [5]]
```

#### `shuffle_data(data)` → array
Shuffle data (deterministic for now).
```synapse
let shuffled = shuffle_data(data)
```

---

## Usage Examples

### Example 1: Data Analysis with synapse-math

```synapse
import "stdlib/math.syn"

// Load data
let data = [12, 15, 18, 20, 22, 25, 28, 30]

// Compute statistics
let mean_val = mean(data)
let min_val = min(data)
let max_val = max(data)
let std_val = std(data)

print("Mean: " + mean_val)
print("Min: " + min_val)
print("Max: " + max_val)
print("Std Dev: " + std_val)

// Scale data to [0, 1]
let scaled = scale(data, 1.0 / max_val)
print("Scaled: " + scaled)
```

### Example 2: Agent Coordination

```synapse
import "stdlib/agents.syn"

// Create agent pool
let agents = create_agent_pool(3)

// Distribute tasks
let task_success = distribute_task(agents, 1, "task1")
let task_success = distribute_task(agents, 2, "task2")
let task_success = distribute_task(agents, 3, "task3")

// Check load
let agent1 = agents[0]
let load = agent_load(agent1)
print("Agent 1 load: " + load)

// Consensus among agents
let votes = [1, 1, 0]  // Three agents voting
let decision = consensus_majority(votes)
print("Team decision: " + decision)
```

### Example 3: Linear Regression

```synapse
import "stdlib/math.syn"
import "stdlib/ml.syn"

// Create model
let model = create_model("linear", 3, 1)
let model = init_weights(model)

// Training data
let x_train = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
let y_train = [10, 14, 18]

// Simple training loop (1 epoch)
let batches = create_batches(x_train, 2)
let i = 0
while i < 99999 {
    try {
        let batch = batches[i]
        let model = gradient_descent_step(model, batch, y_train, linear_mse_loss)
        i = i + 1
    } catch (e) {
        i = 99999
    }
}

// Make prediction
let x_test = [2, 3, 4]
let pred = linear_predict(model, x_test)
print("Prediction: " + pred)
```

### Example 4: Multi-Agent Learning

```synapse
import "stdlib/agents.syn"
import "stdlib/ml.syn"

// Create agent team
let team = create_agent_pool(5)

// Each agent trains a model
let models = []
let i = 0
while i < 5 {
    try {
        let agent = team[i]
        let model = create_model("linear", 4, 1)
        let model = init_weights(model)
        models = models + [model]
        i = i + 1
    } catch (e) {
        i = 99999
    }
}

// Agents make individual predictions
let test_input = [1, 2, 3, 4]
let predictions = []
let j = 0
while j < 99999 {
    try {
        let model = models[j]
        let pred = linear_predict(model, test_input)
        predictions = predictions + [pred]
        j = j + 1
    } catch (e) {
        j = 99999
    }
}

print("Individual predictions: " + predictions)
```

---

## Performance Characteristics

| Function | Time Complexity | Space Complexity | Notes |
|----------|-----------------|------------------|-------|
| `zeros(n)` | O(n) | O(n) | Creates new array |
| `sum(arr)` | O(n) | O(1) | Single pass |
| `mean(arr)` | O(n) | O(1) | Single pass |
| `dot(v1, v2)` | O(n) | O(1) | Single pass |
| `matmul(A, B)` | O(n³) | O(n²) | Standard matmul |
| `flatten(matrix)` | O(n*m) | O(n*m) | Copies all elements |
| `create_agent(...)` | O(1) | O(1) | Constant time |
| `accuracy(...)` | O(n) | O(1) | Single pass |
| `softmax(logits)` | O(n) | O(n) | Needs full array |

---

## Known Limitations

1. **No NumPy/PyTorch Backend**: All operations use native Synapse arrays
2. **Limited Precision**: Floating-point operations use basic approximations
3. **No GPU Acceleration**: Pure CPU-based computation
4. **Simplified ML**: Training uses basic gradient descent without batching
5. **Memory Overhead**: Functional arrays create copies frequently

---

## Future Enhancements

- [ ] GPU backend via LLVM
- [ ] Advanced optimizers (Adam, RMSprop)
- [ ] Neural network layers (Dense, Conv, LSTM)
- [ ] Distributed training across agents
- [ ] Automatic differentiation
- [ ] Type-checked module system

---

## Testing

Comprehensive tests are in `tests/test_phase15_2_stdlib.py`:

```bash
# Run all stdlib tests
pytest tests/test_phase15_2_stdlib.py -v

# Run specific module tests
pytest tests/test_phase15_2_stdlib.py::TestSynapseMathModule -v
pytest tests/test_phase15_2_stdlib.py::TestSynapseAgentsModule -v
pytest tests/test_phase15_2_stdlib.py::TestSynapseMLModule -v

# Run specific test
pytest tests/test_phase15_2_stdlib.py::TestSynapseMathModule::test_dot -v
```

---

## Contributing

To add new functions to stdlib:

1. Add function to appropriate `.syn` file
2. Write tests in `tests/test_phase15_2_stdlib.py`
3. Update documentation in this guide
4. Run full test suite to ensure no regressions

---

**End of Standard Library Guide**
