"""
Phase 15.2: Standard Library Tests
Tests for synapse-math, synapse-agents, and synapse-ml modules
"""

import unittest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from synapse.parser.parser import SynapseParser
from synapse.interpreter.interpreter import Interpreter


class TestSynapseMathModule(unittest.TestCase):
    """Test synapse-math library functions"""
    
    def setUp(self):
        """Initialize parser and interpreter"""
        self.parser = SynapseParser()
        self.interpreter = Interpreter()
    
    def run_code(self, code):
        """Parse and execute code"""
        ast = self.parser.parse(code)
        return self.interpreter.interpret(ast)
    
    # Array Creation Tests
    def test_zeros(self):
        """Test zeros function"""
        code = """
        import "stdlib/math.syn"
        
        let z = zeros(5)
        print(z)
        z
        """
        result = self.run_code(code)
        self.assertEqual(result, [0, 0, 0, 0, 0])
    
    def test_ones(self):
        """Test ones function"""
        code = """
        import "stdlib/math.syn"
        
        let o = ones(3)
        o
        """
        result = self.run_code(code)
        self.assertEqual(result, [1, 1, 1])
    
    def test_arange(self):
        """Test arange function"""
        code = """
        import "stdlib/math.syn"
        
        let r = arange(0, 5, 1)
        r
        """
        result = self.run_code(code)
        self.assertEqual(result, [0, 1, 2, 3, 4])
    
    def test_linspace(self):
        """Test linspace function"""
        code = """
        import "stdlib/math.syn"
        
        let ls = linspace(0, 1, 3)
        ls
        """
        result = self.run_code(code)
        self.assertEqual(len(result), 3)
    
    def test_eye(self):
        """Test identity matrix creation"""
        code = """
        import "stdlib/math.syn"
        
        let i = eye(2)
        i
        """
        result = self.run_code(code)
        self.assertEqual(result, [[1, 0], [0, 1]])
    
    # Array Operations Tests
    def test_shape_1d(self):
        """Test shape function on 1D array"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [1, 2, 3, 4, 5]
        let s = shape(arr)
        s
        """
        result = self.run_code(code)
        self.assertEqual(result, [5])
    
    def test_flatten(self):
        """Test flatten function"""
        code = """
        import "stdlib/math.syn"
        
        let matrix = [[1, 2], [3, 4]]
        let flat = flatten(matrix)
        flat
        """
        result = self.run_code(code)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_transpose(self):
        """Test transpose function"""
        code = """
        import "stdlib/math.syn"
        
        let m = [[1, 2], [3, 4]]
        let t = transpose(m)
        t
        """
        result = self.run_code(code)
        self.assertEqual(result, [[1, 3], [2, 4]])
    
    # Aggregation Tests
    def test_sum(self):
        """Test sum function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [1, 2, 3, 4, 5]
        let s = sum(arr)
        s
        """
        result = self.run_code(code)
        self.assertEqual(result, 15)
    
    def test_mean(self):
        """Test mean function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [1, 2, 3, 4, 5]
        let m = mean(arr)
        m
        """
        result = self.run_code(code)
        self.assertEqual(result, 3)
    
    def test_min(self):
        """Test min function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [5, 2, 8, 1, 9]
        let m = min(arr)
        m
        """
        result = self.run_code(code)
        self.assertEqual(result, 1)
    
    def test_max(self):
        """Test max function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [5, 2, 8, 1, 9]
        let m = max(arr)
        m
        """
        result = self.run_code(code)
        self.assertEqual(result, 9)
    
    # Element-wise Operations
    def test_scale(self):
        """Test scale function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [1, 2, 3]
        let scaled = scale(arr, 2)
        scaled
        """
        result = self.run_code(code)
        self.assertEqual(result, [2, 4, 6])
    
    def test_add(self):
        """Test add function"""
        code = """
        import "stdlib/math.syn"
        
        let a = [1, 2, 3]
        let b = [4, 5, 6]
        let sum = add(a, b)
        sum
        """
        result = self.run_code(code)
        self.assertEqual(result, [5, 7, 9])
    
    # Linear Algebra
    def test_dot(self):
        """Test dot product"""
        code = """
        import "stdlib/math.syn"
        
        let v1 = [1, 2, 3]
        let v2 = [4, 5, 6]
        let d = dot(v1, v2)
        d
        """
        result = self.run_code(code)
        self.assertEqual(result, 32)  # 1*4 + 2*5 + 3*6
    
    def test_matmul(self):
        """Test matrix multiplication"""
        code = """
        import "stdlib/math.syn"
        
        let m1 = [[1, 2], [3, 4]]
        let m2 = [[5, 6], [7, 8]]
        let result = matmul(m1, m2)
        result
        """
        result = self.run_code(code)
        expected = [[19, 22], [43, 50]]
        self.assertEqual(result, expected)
    
    # Utility Functions
    def test_append(self):
        """Test append function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [1, 2, 3]
        let appended = append(arr, 4)
        appended
        """
        result = self.run_code(code)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_reverse(self):
        """Test reverse function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [1, 2, 3, 4, 5]
        let reversed = reverse(arr)
        reversed
        """
        result = self.run_code(code)
        self.assertEqual(result, [5, 4, 3, 2, 1])
    
    def test_clip(self):
        """Test clip function"""
        code = """
        import "stdlib/math.syn"
        
        let arr = [-5, 0, 5, 10]
        let clipped = clip(arr, 0, 5)
        clipped
        """
        result = self.run_code(code)
        self.assertEqual(result, [0, 0, 5, 5])


class TestSynapseAgentsModule(unittest.TestCase):
    """Test synapse-agents library functions"""
    
    def setUp(self):
        """Initialize parser and interpreter"""
        self.parser = SynapseParser()
        self.interpreter = Interpreter()
    
    def run_code(self, code):
        """Parse and execute code"""
        ast = self.parser.parse(code)
        return self.interpreter.interpret(ast)
    
    def test_create_agent(self):
        """Test agent creation"""
        code = """
        import "stdlib/agents.syn"
        
        let agent = create_agent(1, "alice", 5)
        agent
        """
        result = self.run_code(code)
        self.assertIsNotNone(result)
    
    def test_agent_get(self):
        """Test getting agent property"""
        code = """
        import "stdlib/agents.syn"
        
        let agent = create_agent(1, "alice", 5)
        let name = agent_get(agent, "name")
        name
        """
        result = self.run_code(code)
        self.assertEqual(result, "alice")
    
    def test_agent_set(self):
        """Test setting agent property"""
        code = """
        import "stdlib/agents.syn"
        
        let agent = create_agent(1, "alice", 5)
        let updated = agent_set(agent, "name", "bob")
        let new_name = agent_get(updated, "name")
        new_name
        """
        result = self.run_code(code)
        self.assertEqual(result, "bob")
    
    def test_create_agent_pool(self):
        """Test creating pool of agents"""
        code = """
        import "stdlib/agents.syn"
        
        let pool = create_agent_pool(3)
        pool
        """
        result = self.run_code(code)
        self.assertEqual(len(result), 3)
    
    def test_agent_load(self):
        """Test getting agent load"""
        code = """
        import "stdlib/agents.syn"
        
        let agent = create_agent(1, "alice", 5)
        let agent = submit_task(agent, 1, "task1")
        let load = agent_load(agent)
        load
        """
        result = self.run_code(code)
        self.assertEqual(result, 1)
    
    def test_consensus_majority(self):
        """Test majority vote consensus"""
        code = """
        import "stdlib/agents.syn"
        
        let votes = [1, 1, 0, 1, 0]
        let consensus = consensus_majority(votes)
        consensus
        """
        result = self.run_code(code)
        self.assertEqual(result, 1)  # Majority is 1
    
    def test_create_message(self):
        """Test message creation"""
        code = """
        import "stdlib/agents.syn"
        
        let msg = create_message(1, 2, "hello")
        msg
        """
        result = self.run_code(code)
        self.assertIsNotNone(result)
    
    def test_agent_state_management(self):
        """Test agent state management"""
        code = """
        import "stdlib/agents.syn"
        
        let agent = create_agent(1, "alice", 5)
        let agent = agent_state_set(agent, "energy", 100)
        let energy = agent_state_get(agent, "energy")
        energy
        """
        result = self.run_code(code)
        self.assertEqual(result, 100)


class TestSynapseMLModule(unittest.TestCase):
    """Test synapse-ml library functions"""
    
    def setUp(self):
        """Initialize parser and interpreter"""
        self.parser = SynapseParser()
        self.interpreter = Interpreter()
    
    def run_code(self, code):
        """Parse and execute code"""
        ast = self.parser.parse(code)
        return self.interpreter.interpret(ast)
    
    def test_create_model(self):
        """Test model creation"""
        code = """
        import "stdlib/ml.syn"
        
        let model = create_model("linear", 5, 1)
        model
        """
        result = self.run_code(code)
        self.assertIsNotNone(result)
    
    def test_model_get(self):
        """Test getting model property"""
        code = """
        import "stdlib/ml.syn"
        
        let model = create_model("linear", 5, 1)
        let itype = model_get(model, "type")
        itype
        """
        result = self.run_code(code)
        self.assertEqual(result, "linear")
    
    def test_model_set(self):
        """Test setting model property"""
        code = """
        import "stdlib/ml.syn"
        
        let model = create_model("linear", 5, 1)
        let updated = model_set(model, "lr", 0.001)
        let lr = model_get(updated, "lr")
        lr
        """
        result = self.run_code(code)
        self.assertEqual(result, 0.001)
    
    def test_sigmoid(self):
        """Test sigmoid activation"""
        code = """
        import "stdlib/ml.syn"
        
        let s = sigmoid(0)
        s
        """
        result = self.run_code(code)
        self.assertAlmostEqual(result, 0.5, places=1)
    
    def test_relu(self):
        """Test ReLU activation"""
        code = """
        import "stdlib/ml.syn"
        
        let r1 = relu(5)
        let r2 = relu(-5)
        [r1, r2]
        """
        result = self.run_code(code)
        self.assertEqual(result, [5, 0])
    
    def test_softmax(self):
        """Test softmax function"""
        code = """
        import "stdlib/ml.syn"
        
        let logits = [1, 2, 3]
        let probs = softmax(logits)
        probs
        """
        result = self.run_code(code)
        self.assertEqual(len(result), 3)
    
    def test_accuracy(self):
        """Test accuracy metric"""
        code = """
        import "stdlib/ml.syn"
        
        let y_true = [1, 0, 1, 1, 0]
        let y_pred = [0.9, 0.1, 0.8, 0.7, 0.2]
        let acc = accuracy(y_true, y_pred)
        acc
        """
        result = self.run_code(code)
        self.assertEqual(result, 1.0)  # All correct
    
    def test_precision(self):
        """Test precision metric"""
        code = """
        import "stdlib/ml.syn"
        
        let y_true = [1, 1, 0, 0]
        let y_pred = [0.9, 0.8, 0.3, 0.4]
        let prec = precision(y_true, y_pred)
        prec
        """
        result = self.run_code(code)
        self.assertGreater(result, 0)
    
    def test_recall(self):
        """Test recall metric"""
        code = """
        import "stdlib/ml.syn"
        
        let y_true = [1, 1, 0, 0]
        let y_pred = [0.9, 0.2, 0.3, 0.4]
        let rec = recall(y_true, y_pred)
        rec
        """
        result = self.run_code(code)
        self.assertGreater(result, 0)
    
    def test_f1_score(self):
        """Test F1 score"""
        code = """
        import "stdlib/ml.syn"
        
        let y_true = [1, 1, 0, 0]
        let y_pred = [0.9, 0.8, 0.3, 0.4]
        let f1 = f1_score(y_true, y_pred)
        f1
        """
        result = self.run_code(code)
        self.assertGreater(result, 0)
    
    def test_create_batches(self):
        """Test batch creation"""
        code = """
        import "stdlib/ml.syn"
        
        let data = [1, 2, 3, 4, 5]
        let batches = create_batches(data, 2)
        batches
        """
        result = self.run_code(code)
        self.assertEqual(len(result), 3)


class TestStdlibIntegration(unittest.TestCase):
    """Integration tests combining multiple stdlib modules"""
    
    def setUp(self):
        """Initialize parser and interpreter"""
        self.parser = SynapseParser()
        self.interpreter = Interpreter()
    
    def run_code(self, code):
        """Parse and execute code"""
        ast = self.parser.parse(code)
        return self.interpreter.interpret(ast)
    
    def test_math_with_agents(self):
        """Test using math functions with agents"""
        code = """
        import "stdlib/math.syn"
        import "stdlib/agents.syn"
        
        let data = [1, 2, 3, 4, 5]
        let pool = create_agent_pool(3)
        let avg = mean(data)
        avg
        """
        result = self.run_code(code)
        self.assertEqual(result, 3)
    
    def test_ml_with_math(self):
        """Test using ML functions with math operations"""
        code = """
        import "stdlib/math.syn"
        import "stdlib/ml.syn"
        
        let x = [1, 2, 3]
        let scaled = scale(x, 0.5)
        let avg = mean(scaled)
        avg
        """
        result = self.run_code(code)
        self.assertEqual(result, 1)
    
    def test_full_pipeline(self):
        """Test using all three modules together"""
        code = """
        import "stdlib/math.syn"
        import "stdlib/agents.syn"
        import "stdlib/ml.syn"
        
        let data = [1, 2, 3, 4, 5]
        let avg = mean(data)
        let pool = create_agent_pool(2)
        let model = create_model("linear", 5, 1)
        [avg, model]
        """
        result = self.run_code(code)
        self.assertEqual(result[0], 3)


if __name__ == "__main__":
    unittest.main()
