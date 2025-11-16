# Synapse Standard Library (stdlib)

**Version:** 1.0  
**Date:** November 16, 2025  
**Status:** Complete and Production-Ready  

---

## Overview

The Synapse Standard Library provides three comprehensive modules for common programming tasks in Synapse:

1. **synapse-math** - Numerical computing with NumPy-like operations
2. **synapse-agents** - Multi-agent systems framework
3. **synapse-ml** - Machine learning helpers

All modules are written in pure Synapse and fully integrated with the language.

---

## Quick Start

### Import a Module

```synapse
import "stdlib/math.syn"
```

### Use Functions

```synapse
import "stdlib/math.syn"

let arr = [1, 2, 3, 4, 5]
let avg = mean(arr)
let summed = sum(arr)
print("Average: " + avg)
print("Sum: " + summed)
```

---

## Module Reference

### synapse-math

**File:** `math.syn` (620 lines, 40 functions)

Numerical computing and array operations.

#### Quick Examples

```synapse
import "stdlib/math.syn"

// Create arrays
let zeros_arr = zeros(5)        // [0, 0, 0, 0, 0]
let ones_arr = ones(3)          // [1, 1, 1]
let range_arr = arange(0, 5, 1) // [0, 1, 2, 3, 4]

// Aggregate operations
let sum_val = sum([1, 2, 3, 4, 5])     // 15
let mean_val = mean([1, 2, 3, 4, 5])   // 3
let min_val = min([5, 2, 8, 1, 9])     // 1
let max_val = max([5, 2, 8, 1, 9])     // 9

// Element-wise operations
let scaled = scale([1, 2, 3], 2)       // [2, 4, 6]
let added = add([1, 2, 3], [4, 5, 6])  // [5, 7, 9]

// Linear algebra
let v1 = [1, 2, 3]
let v2 = [4, 5, 6]
let dot_product = dot(v1, v2)  // 32

// Matrix operations
let m1 = [[1, 2], [3, 4]]
let m2 = [[5, 6], [7, 8]]
let product = matmul(m1, m2)   // [[19, 22], [43, 50]]
```

**Function Categories:**
- Array Creation: zeros, ones, arange, linspace, eye
- Array Operations: shape, flatten, reshape, transpose
- Aggregations: sum, mean, min, max, std
- Element-wise: add, multiply, scale
- Linear Algebra: dot, matmul, norm
- Utilities: append, insert, reverse, clip

### synapse-agents

**File:** `agents.syn` (450 lines, 25 functions)

Framework for building multi-agent systems.

#### Quick Examples

```synapse
import "stdlib/agents.syn"

// Create agents
let agent = create_agent(1, "alice", 10)
let pool = create_agent_pool(3)

// Task management
let agent = submit_task(agent, 1, "task_data")
let load = agent_load(agent)
let agent = complete_task(agent, 1)

// Consensus voting
let votes = [1, 1, 0, 1, 0]
let decision = consensus_majority(votes)  // 1 (majority)

// Agent pool coordination
let available = find_available_agent(pool)
let success = distribute_task(pool, 1, "new_task")
```

**Function Categories:**
- Agent Management: create_agent, create_agent_pool, agent_get, agent_set
- Task Management: submit_task, get_pending_tasks, complete_task
- Scheduling: distribute_task, find_available_agent, balance_tasks
- Consensus: consensus_majority, consensus_weighted
- Communication: create_message, send_message
- State: agent_state_set, agent_state_get

### synapse-ml

**File:** `ml.syn` (550 lines, 30 functions)

Machine learning helpers and model utilities.

#### Quick Examples

```synapse
import "stdlib/ml.syn"

// Create and configure model
let model = create_model("linear", 5, 1)
let model = model_set(model, "lr", 0.001)
let model = init_weights(model)

// Make predictions
let x = [1, 2, 3, 4, 5]
let pred = linear_predict(model, x)

// Evaluate model
let y_true = [1, 0, 1, 1, 0]
let y_pred = [0.9, 0.1, 0.8, 0.7, 0.2]
let acc = accuracy(y_true, y_pred)
let prec = precision(y_true, y_pred)
let rec = recall(y_true, y_pred)
let f1 = f1_score(y_true, y_pred)

// Activation functions
let s = sigmoid(0)      // ~0.5
let r = relu(5)         // 5
let p = softmax([1, 2]) // [0.27, 0.73]
```

**Function Categories:**
- Model Management: create_model, model_get, model_set, init_weights
- Activations: sigmoid, relu, tanh_approx, softmax
- Loss Functions: linear_mse_loss, logistic_loss
- Prediction: linear_predict, logistic_predict
- Metrics: accuracy, precision, recall, f1_score
- Training: gradient_descent_step
- Data: create_batches, shuffle_data

---

## Documentation

### Comprehensive Guide

For detailed documentation of all functions and examples, see:

📖 **File:** `../docs/STDLIB_GUIDE.md` (850+ lines)

Includes:
- Function reference for all 95+ functions
- Usage examples for each function
- Performance characteristics
- Known limitations
- Future enhancements

### Examples

Working examples demonstrating all three modules:

📝 **File:** `../examples/stdlib_examples.syn`

Includes 10 example programs:
1. Data analysis
2. Array operations
3. Linear algebra
4. Agent coordination
5. Consensus voting
6. Model creation
7. Activation functions
8. Classification metrics
9. Data batching
10. Multi-module combined example

---

## Testing

Comprehensive test suite for all stdlib modules:

🧪 **File:** `../tests/test_phase15_2_stdlib.py`

**Coverage:**
- 34 test cases across all modules
- 4 test suites (Math, Agents, ML, Integration)
- 100% of major functions tested

**Run Tests:**
```bash
# All tests
pytest tests/test_phase15_2_stdlib.py -v

# Specific module
pytest tests/test_phase15_2_stdlib.py::TestSynapseMathModule -v

# Specific test
pytest tests/test_phase15_2_stdlib.py::TestSynapseMathModule::test_sum -v
```

---

## File Structure

```
stdlib/
├── README.md              (this file)
├── math.syn              (synapse-math module)
├── agents.syn            (synapse-agents module)
└── ml.syn                (synapse-ml module)

docs/
└── STDLIB_GUIDE.md       (comprehensive guide)

examples/
└── stdlib_examples.syn   (usage examples)

tests/
└── test_phase15_2_stdlib.py  (test suite)
```

---

## Design Philosophy

### 1. Pure Synapse Implementation
All stdlib modules are written in Synapse itself, demonstrating the language's completeness and power.

### 2. Functional Programming
Functions are pure and immutable:
- Return new arrays instead of modifying in-place
- No hidden state changes
- Composable operations

### 3. NumPy Compatibility
Function names and semantics match NumPy where applicable, making it easy for Python developers.

### 4. Performance
While using interpreted Synapse, the stdlib is designed to be as efficient as possible:
- Minimal intermediate allocations
- Direct loop implementations
- Numerical stability (e.g., sigmoid clipping)

### 5. Accessibility
Comprehensive documentation and examples make it easy to learn and use.

---

## Usage Patterns

### Pattern 1: Data Analysis Pipeline

```synapse
import "stdlib/math.syn"

// Load and process data
let raw_data = [12, 15, 18, 20, 22, 25, 28, 30]
let normalized = scale(raw_data, 1.0 / max(raw_data))
let stats = [mean(raw_data), std(raw_data)]
```

### Pattern 2: Agent-Based Simulation

```synapse
import "stdlib/agents.syn"

// Create team
let team = create_agent_pool(5)

// Assign work
let i = 0
while i < 5 {
    try {
        distribute_task(team, i, "task_" + i)
        i = i + 1
    } catch (e) {
        i = 99999
    }
}
```

### Pattern 3: Machine Learning Pipeline

```synapse
import "stdlib/ml.syn"

// Setup
let model = create_model("linear", 3, 1)
let model = init_weights(model)

// Train (simplified)
let x_train = [[1, 2, 3]]
let y_train = [10]
let model = gradient_descent_step(model, x_train, y_train, linear_mse_loss)

// Evaluate
let y_pred = [linear_predict(model, [1, 2, 3])]
let acc = accuracy(y_train, y_pred)
```

---

## Performance Characteristics

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| zeros(n) | O(n) | Creates array |
| sum(arr) | O(n) | Single pass |
| dot(v1, v2) | O(n) | Vector operations |
| matmul(A, B) | O(n³) | Standard algorithm |
| sort/shuffle | O(n log n) | Not optimized yet |

---

## Known Limitations

1. **No native optimization** - Pure Synapse, not as fast as NumPy
2. **Limited precision** - Uses basic float approximations
3. **No GPU backend** - CPU only
4. **Simplified ML** - Basic algorithms, no advanced optimizers
5. **Memory overhead** - Functional style creates copies

---

## Future Enhancements

- [ ] GPU acceleration via LLVM
- [ ] Advanced optimizers (Adam, RMSprop)
- [ ] Neural network layers (Dense, Conv, etc.)
- [ ] Distributed training
- [ ] Automatic differentiation
- [ ] Type-checked imports

---

## Contributing

To add functions to stdlib:

1. **Add function** to appropriate module (.syn file)
2. **Add tests** to test_phase15_2_stdlib.py
3. **Update docs** in STDLIB_GUIDE.md
4. **Run test suite** to ensure no regressions

---

## Support

- 📖 Full documentation: `docs/STDLIB_GUIDE.md`
- 📝 Code examples: `examples/stdlib_examples.syn`
- 🧪 Tests: `tests/test_phase15_2_stdlib.py`
- 💬 Issues: Contact project maintainer

---

## Version History

### v1.0 (November 16, 2025)
- Initial release
- 3 modules: math, agents, ml
- 95+ functions
- 34 tests
- 850+ lines documentation

---

## License

Synapse Standard Library is part of the Synapse project and follows the same license.

---

**End of README**

For more information, see `../docs/STDLIB_GUIDE.md`
