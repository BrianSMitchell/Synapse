# Synapse API Documentation

*Generated: 2025-11-16 09:11:29*

## Table of Contents

- [agents](#agents)
  - [create_agent](#create_agent)
  - [agent_get](#agent_get)
  - [agent_set](#agent_set)
  - [submit_task](#submit_task)
  - [get_pending_tasks](#get_pending_tasks)
  - [complete_task](#complete_task)
  - [has_capacity](#has_capacity)
  - [create_agent_pool](#create_agent_pool)
  - [find_available_agent](#find_available_agent)
  - [distribute_task](#distribute_task)
  - [agent_load](#agent_load)
  - [balance_tasks](#balance_tasks)
  - [consensus_majority](#consensus_majority)
  - [consensus_weighted](#consensus_weighted)
  - [create_message](#create_message)
  - [send_message](#send_message)
  - [agent_state_set](#agent_state_set)
  - [agent_state_get](#agent_state_get)
- [math](#math)
  - [zeros](#zeros)
  - [ones](#ones)
  - [arange](#arange)
  - [linspace](#linspace)
  - [eye](#eye)
  - [shape](#shape)
  - [flatten](#flatten)
  - [reshape](#reshape)
  - [transpose](#transpose)
  - [sum](#sum)
  - [mean](#mean)
  - [min](#min)
  - [max](#max)
  - [std](#std)
  - [add](#add)
  - [multiply](#multiply)
  - [scale](#scale)
  - [dot](#dot)
  - [matmul](#matmul)
  - [norm](#norm)
  - [append](#append)
  - [insert](#insert)
  - [reverse](#reverse)
  - [clip](#clip)
- [ml](#ml)
  - [create_model](#create_model)
  - [model_get](#model_get)
  - [model_set](#model_set)
  - [init_weights](#init_weights)
  - [linear_predict](#linear_predict)
  - [linear_mse_loss](#linear_mse_loss)
  - [sigmoid](#sigmoid)
  - [logistic_predict](#logistic_predict)
  - [logistic_loss](#logistic_loss)
  - [relu](#relu)
  - [relu_derivative](#relu_derivative)
  - [tanh_approx](#tanh_approx)
  - [softmax](#softmax)
  - [accuracy](#accuracy)
  - [precision](#precision)
  - [recall](#recall)
  - [f1_score](#f1_score)
  - [gradient_descent_step](#gradient_descent_step)
  - [create_batches](#create_batches)
  - [shuffle_data](#shuffle_data)


## agents

SYNAPSE-AGENTS: Standard Library Module for Multi-Agent Systems
Agent framework for building distributed, cooperative, and emergent systems
Features: agent creation, task scheduling, consensus, communication
Version: 1.0
AGENT DATA STRUCTURES

### Functions

#### `create_agent(`id`, `name`, `capacity`)`

**Parameters:**

- `id`
- `name`
- `capacity`


#### `agent_get(`agent`, `key`)`

**Parameters:**

- `agent`
- `key`


#### `agent_set(`agent`, `key`, `value`)`

**Parameters:**

- `agent`
- `key`
- `value`


#### `submit_task(`agent`, `task_id`, `task_data`)`

**Parameters:**

- `agent`
- `task_id`
- `task_data`


#### `get_pending_tasks(`agent`)`

**Parameters:**

- `agent`


#### `complete_task(`agent`, `task_id`)`

**Parameters:**

- `agent`
- `task_id`


#### `has_capacity(`agent`)`

**Parameters:**

- `agent`


#### `create_agent_pool(`count`)`

**Parameters:**

- `count`


#### `find_available_agent(`agents`)`

**Parameters:**

- `agents`


#### `distribute_task(`agents`, `task_id`, `task_data`)`

**Parameters:**

- `agents`
- `task_id`
- `task_data`


#### `agent_load(`agent`)`

**Parameters:**

- `agent`


#### `balance_tasks(`agents`)`

**Parameters:**

- `agents`


#### `consensus_majority(`votes`)`

**Parameters:**

- `votes`


#### `consensus_weighted(`votes`, `weights`)`

**Parameters:**

- `votes`
- `weights`


#### `create_message(`sender_id`, `receiver_id`, `content`)`

**Parameters:**

- `sender_id`
- `receiver_id`
- `content`


#### `send_message(`agents`, `message`)`

**Parameters:**

- `agents`
- `message`


#### `agent_state_set(`agent`, `key`, `value`)`

**Parameters:**

- `agent`
- `key`
- `value`


#### `agent_state_get(`agent`, `key`)`

**Parameters:**

- `agent`
- `key`



## math

SYNAPSE-MATH: Standard Library Module for Numerical Computing
NumPy-like array operations for mathematical computation in Synapse
Features: array creation, basic operations, linear algebra, aggregations
Version: 1.0
ARRAY CREATION FUNCTIONS

### Functions

#### `zeros(`n`)`

**Parameters:**

- `n`


#### `ones(`n`)`

**Parameters:**

- `n`


#### `arange(`start`, `end`, `step`)`

**Parameters:**

- `start`
- `end`
- `step`


#### `linspace(`start`, `end`, `count`)`

**Parameters:**

- `start`
- `end`
- `count`


#### `eye(`n`)`

**Parameters:**

- `n`


#### `shape(`arr`)`

**Parameters:**

- `arr`


#### `flatten(`matrix`)`

**Parameters:**

- `matrix`


#### `reshape(`arr`, `shape_tuple`)`

**Parameters:**

- `arr`
- `shape_tuple`


#### `transpose(`matrix`)`

**Parameters:**

- `matrix`


#### `sum(`arr`)`

**Parameters:**

- `arr`


#### `mean(`arr`)`

**Parameters:**

- `arr`


#### `min(`arr`)`

**Parameters:**

- `arr`


#### `max(`arr`)`

**Parameters:**

- `arr`


#### `std(`arr`)`

**Parameters:**

- `arr`


#### `add(`arr1`, `arr2`)`

**Parameters:**

- `arr1`
- `arr2`


#### `multiply(`arr1`, `arr2`)`

**Parameters:**

- `arr1`
- `arr2`


#### `scale(`arr`, `factor`)`

**Parameters:**

- `arr`
- `factor`


#### `dot(`vec1`, `vec2`)`

**Parameters:**

- `vec1`
- `vec2`


#### `matmul(`mat1`, `mat2`)`

**Parameters:**

- `mat1`
- `mat2`


#### `norm(`vec`)`

**Parameters:**

- `vec`


#### `append(`arr`, `value`)`

**Parameters:**

- `arr`
- `value`


#### `insert(`arr`, `idx`, `value`)`

**Parameters:**

- `arr`
- `idx`
- `value`


#### `reverse(`arr`)`

**Parameters:**

- `arr`


#### `clip(`arr`, `min_val`, `max_val`)`

**Parameters:**

- `arr`
- `min_val`
- `max_val`



## ml

SYNAPSE-ML: Standard Library Module for Machine Learning
ML helpers for classification, regression, and probabilistic modeling
Features: model creation, training, inference, evaluation metrics
Version: 1.0
MODEL STRUCTURE AND INITIALIZATION

### Functions

#### `create_model(`model_type`, `input_dim`, `output_dim`)`

**Parameters:**

- `model_type`
- `input_dim`
- `output_dim`


#### `model_get(`model`, `key`)`

**Parameters:**

- `model`
- `key`


#### `model_set(`model`, `key`, `value`)`

**Parameters:**

- `model`
- `key`
- `value`


#### `init_weights(`model`)`

**Parameters:**

- `model`


#### `linear_predict(`model`, `x`)`

**Parameters:**

- `model`
- `x`


#### `linear_mse_loss(`y_true`, `y_pred`)`

**Parameters:**

- `y_true`
- `y_pred`


#### `sigmoid(`x`)`

**Parameters:**

- `x`


#### `logistic_predict(`model`, `x`)`

**Parameters:**

- `model`
- `x`


#### `logistic_loss(`y_true`, `y_pred`)`

**Parameters:**

- `y_true`
- `y_pred`


#### `relu(`x`)`

**Parameters:**

- `x`


#### `relu_derivative(`x`)`

**Parameters:**

- `x`


#### `tanh_approx(`x`)`

**Parameters:**

- `x`


#### `softmax(`logits`)`

**Parameters:**

- `logits`


#### `accuracy(`y_true`, `y_pred`)`

**Parameters:**

- `y_true`
- `y_pred`


#### `precision(`y_true`, `y_pred`)`

**Parameters:**

- `y_true`
- `y_pred`


#### `recall(`y_true`, `y_pred`)`

**Parameters:**

- `y_true`
- `y_pred`


#### `f1_score(`y_true`, `y_pred`)`

**Parameters:**

- `y_true`
- `y_pred`


#### `gradient_descent_step(`model`, `x_batch`, `y_batch`, `loss_fn`)`

**Parameters:**

- `model`
- `x_batch`
- `y_batch`
- `loss_fn`


#### `create_batches(`data`, `batch_size`)`

**Parameters:**

- `data`
- `batch_size`


#### `shuffle_data(`data`)`

**Parameters:**

- `data`

