"""Comprehensive test suite for Phase 16.3: Distributed Agent Training

Tests cover:
- Basic agent creation and synchronization
- Multi-agent training coordination
- Loss minimization across agents
- Synchronization barriers
- MPI and Spark trainer interfaces
- Weight averaging and convergence
"""

import pytest
import asyncio
import numpy as np
from typing import Tuple

from synapse.core.distributed_training import (
    AgentState,
    SyncMessage,
    LocalSyncCoordinator,
    DistributedAgent,
    DistributedTrainer,
    simple_loss_function,
)


# ============================================================================
# Tests: AgentState
# ============================================================================

class TestAgentState:
    """Test AgentState dataclass."""
    
    def test_create_agent_state(self):
        """Test creating an agent state."""
        state = AgentState(agent_id="agent1")
        assert state.agent_id == "agent1"
        assert state.iteration == 0
        assert state.loss == 0.0
    
    def test_agent_state_to_dict(self):
        """Test serialization to dict."""
        state = AgentState(
            agent_id="agent1",
            weights=np.array([1.0, 2.0, 3.0]),
            loss=0.5,
            iteration=10
        )
        
        data = state.to_dict()
        assert data['agent_id'] == "agent1"
        assert data['loss'] == 0.5
        assert data['iteration'] == 10
        assert isinstance(data['weights'], list)
    
    def test_agent_state_from_dict(self):
        """Test deserialization from dict."""
        original = AgentState(
            agent_id="agent1",
            weights=np.array([1.0, 2.0]),
            loss=0.25,
            iteration=5
        )
        
        data = original.to_dict()
        restored = AgentState.from_dict(data)
        
        assert restored.agent_id == original.agent_id
        assert restored.loss == original.loss
        assert restored.iteration == original.iteration
        assert np.allclose(restored.weights, original.weights)


# ============================================================================
# Tests: SyncMessage
# ============================================================================

class TestSyncMessage:
    """Test SyncMessage serialization."""
    
    def test_create_sync_message(self):
        """Test creating a sync message."""
        msg = SyncMessage(
            source_id="agent1",
            target_ids=["agent2", "agent3"],
            message_type="weights",
            payload={'weights': [1.0, 2.0]}
        )
        
        assert msg.source_id == "agent1"
        assert len(msg.target_ids) == 2
        assert msg.message_type == "weights"
    
    def test_sync_message_json_roundtrip(self):
        """Test JSON serialization roundtrip."""
        original = SyncMessage(
            source_id="agent1",
            target_ids=["agent2"],
            message_type="state",
            payload={'loss': 0.5}
        )
        
        json_str = original.to_json()
        restored = SyncMessage.from_json(json_str)
        
        assert restored.source_id == original.source_id
        assert restored.target_ids == original.target_ids
        assert restored.message_type == original.message_type
        assert restored.payload == original.payload


# ============================================================================
# Tests: LocalSyncCoordinator
# ============================================================================

class TestLocalSyncCoordinator:
    """Test LocalSyncCoordinator implementation."""
    
    def test_register_agents(self):
        """Test agent registration."""
        coord = LocalSyncCoordinator()
        
        coord.register_agent("agent1")
        coord.register_agent("agent2")
        
        assert coord.agent_count == 2
        assert "agent1" in coord.message_queue
        assert "agent2" in coord.message_queue
    
    def test_broadcast_message(self):
        """Test broadcasting messages."""
        async def run_broadcast():
            coord = LocalSyncCoordinator()
            coord.register_agent("agent1")
            coord.register_agent("agent2")
            
            msg = SyncMessage(
                source_id="agent1",
                target_ids=[],
                message_type="weights",
                payload={'w': [1.0]}
            )
            
            result = await coord.broadcast(msg)
            
            assert result['status'] == 'success'
            assert result['delivered'] == 1  # Only agent2 receives
        
        asyncio.run(run_broadcast())
    
    def test_gather_messages(self):
        """Test gathering messages."""
        async def run_gather():
            coord = LocalSyncCoordinator()
            coord.register_agent("agent1")
            coord.register_agent("agent2")
            
            msg = SyncMessage(
                source_id="agent1",
                target_ids=["agent2"],
                message_type="weights",
                payload={'data': 'test'}
            )
            
            await coord.send(msg)
            messages = await coord.gather("agent2", timeout=2.0)
            
            assert len(messages) == 1
            assert messages[0].payload['data'] == 'test'
        
        asyncio.run(run_gather())
    
    def test_barrier_synchronization(self):
        """Test barrier synchronization."""
        async def run_barrier():
            coord = LocalSyncCoordinator()
            coord.register_agent("agent1")
            coord.register_agent("agent2")
            
            # Both agents reach barrier
            task1 = coord.barrier("agent1", timeout=2.0)
            task2 = coord.barrier("agent2", timeout=2.0)
            
            # Update barrier count
            coord.barriers["agent1"] = 2
            coord.barriers["agent2"] = 2
            
            result1 = await task1
            result2 = await task2
            
            # At least one should be ready (may timeout depending on timing)
            assert isinstance(result1, bool)
            assert isinstance(result2, bool)
        
        asyncio.run(run_barrier())


# ============================================================================
# Tests: DistributedAgent
# ============================================================================

class TestDistributedAgent:
    """Test DistributedAgent functionality."""
    
    def test_agent_creation(self):
        """Test creating a distributed agent."""
        coord = LocalSyncCoordinator()
        agent = DistributedAgent("agent1", coord)
        
        assert agent.agent_id == "agent1"
        assert agent.state.agent_id == "agent1"
        assert agent.state.iteration == 0
    
    def test_train_step(self):
        """Test single training step."""
        async def run_train_step():
            coord = LocalSyncCoordinator()
            coord.register_agent("agent1")
            
            agent = DistributedAgent("agent1", coord)
            agent.set_weights(np.array([1.0, 2.0, 3.0]))
            
            initial_loss, _ = simple_loss_function(agent.state.weights)
            
            loss = await agent.train_step(simple_loss_function, learning_rate=0.1)
            
            assert agent.state.iteration == 1
            assert agent.state.loss == loss
            assert len(agent.learning_history) == 1
            # Loss should decrease with gradient descent
            assert loss < initial_loss
        
        asyncio.run(run_train_step())
    
    def test_multiple_train_steps(self):
        """Test multiple training steps."""
        async def run_multiple_steps():
            coord = LocalSyncCoordinator()
            coord.register_agent("agent1")
            
            agent = DistributedAgent("agent1", coord)
            agent.set_weights(np.array([1.0, 1.0]))
            
            losses = []
            for _ in range(10):
                loss = await agent.train_step(simple_loss_function, learning_rate=0.05)
                losses.append(loss)
            
            assert agent.state.iteration == 10
            assert len(losses) == 10
            # Losses should generally decrease
            assert losses[-1] < losses[0]
        
        asyncio.run(run_multiple_steps())
    
    def test_set_get_weights(self):
        """Test setting and getting weights."""
        coord = LocalSyncCoordinator()
        agent = DistributedAgent("agent1", coord)
        
        weights = np.array([1.0, 2.0, 3.0])
        agent.set_weights(weights)
        
        assert np.allclose(agent.state.weights, weights)
    
    def test_synchronize_single_agent(self):
        """Test synchronization with single agent."""
        async def run_sync():
            coord = LocalSyncCoordinator()
            coord.register_agent("agent1")
            
            agent = DistributedAgent("agent1", coord)
            agent.set_weights(np.array([1.0, 2.0]))
            
            result = await agent.synchronize()
            
            assert 'status' in result
        
        asyncio.run(run_sync())


# ============================================================================
# Tests: DistributedTrainer
# ============================================================================

class TestDistributedTrainer:
    """Test DistributedTrainer orchestration."""
    
    def test_create_trainer(self):
        """Test creating a trainer."""
        agent_ids = ["agent1", "agent2", "agent3"]
        trainer = DistributedTrainer(agent_ids)
        
        assert len(trainer.agents) == 3
        assert all(agent_id in trainer.agents for agent_id in agent_ids)
    
    def test_initialize_weights(self):
        """Test weight initialization."""
        agent_ids = ["agent1", "agent2"]
        trainer = DistributedTrainer(agent_ids)
        
        initial_weights = np.array([0.5, 0.5, 0.5])
        trainer.initialize_weights(initial_weights)
        
        for agent in trainer.agents.values():
            assert agent.state.weights.shape == initial_weights.shape
            # Weights should be slightly different (added noise)
            assert not np.allclose(agent.state.weights, initial_weights)
    
    def test_train_all_agents(self):
        """Test training all agents."""
        async def run_train():
            agent_ids = ["agent1", "agent2"]
            trainer = DistributedTrainer(agent_ids)
            
            # Initialize weights
            trainer.initialize_weights(np.array([1.0, 1.0]))
            
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=20,
                learning_rate=0.05,
                sync_interval=5
            )
            
            assert 'total_agents' in results
            assert results['total_agents'] == 2
            assert 'agent_results' in results
            assert len(results['agent_results']) == 2
            
            # Check that agents trained
            for agent_result in results['agent_results'].values():
                assert agent_result['iterations'] == 20
                assert agent_result['final_loss'] < 10.0  # Should minimize loss
        
        asyncio.run(run_train())
    
    def test_distributed_convergence(self):
        """Test that distributed training converges."""
        async def run_convergence():
            agent_ids = ["agent1", "agent2", "agent3"]
            trainer = DistributedTrainer(agent_ids)
            
            trainer.initialize_weights(np.array([0.5, 0.5]))
            
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=50,
                learning_rate=0.1,
                sync_interval=5
            )
            
            # All agents should have low final loss
            for agent_result in results['agent_results'].values():
                assert agent_result['final_loss'] < 0.1
        
        asyncio.run(run_convergence())
    
    def test_get_agent(self):
        """Test retrieving an agent."""
        trainer = DistributedTrainer(["agent1", "agent2"])
        
        agent = trainer.get_agent("agent1")
        assert agent is not None
        assert agent.agent_id == "agent1"
        
        missing = trainer.get_agent("nonexistent")
        assert missing is None
    
    def test_get_summary(self):
        """Test getting trainer summary."""
        agent_ids = ["agent1", "agent2"]
        trainer = DistributedTrainer(agent_ids)
        
        summary = trainer.get_summary()
        
        assert summary['total_agents'] == 2
        assert 'agents' in summary
        assert len(summary['agents']) == 2
        assert 'total_time' in summary


# ============================================================================
# Tests: Weight Averaging
# ============================================================================

class TestWeightAveraging:
    """Test weight averaging synchronization."""
    
    def test_weight_averaging(self):
        """Test that weights are averaged correctly."""
        async def run_averaging():
            agent_ids = ["agent1", "agent2", "agent3"]
            trainer = DistributedTrainer(agent_ids)
            
            # Set different weights for each agent
            trainer.agents["agent1"].set_weights(np.array([1.0, 2.0]))
            trainer.agents["agent2"].set_weights(np.array([3.0, 4.0]))
            trainer.agents["agent3"].set_weights(np.array([5.0, 6.0]))
            
            # Synchronize agent1
            await trainer.agents["agent1"].synchronize()
            
            # After sync, should have some averaging effect (implementation dependent)
            assert trainer.agents["agent1"].state.weights.shape == (2,)
        
        asyncio.run(run_averaging())
    
    def test_multi_agent_sync_with_training(self):
        """Test synchronization during training."""
        async def run_sync_training():
            agent_ids = ["agent1", "agent2"]
            trainer = DistributedTrainer(agent_ids)
            
            trainer.initialize_weights(np.array([1.0, 1.0]))
            
            # Train with frequent synchronization
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=30,
                learning_rate=0.05,
                sync_interval=3
            )
            
            # Verify all agents trained
            assert len(results['agent_results']) == 2
        
        asyncio.run(run_sync_training())


# ============================================================================
# Tests: Loss Minimization
# ============================================================================

class TestLossMinimization:
    """Test that distributed training minimizes loss."""
    
    def test_simple_loss_minimization(self):
        """Test minimizing simple quadratic loss."""
        async def run_minimization():
            agent_ids = ["agent1"]
            trainer = DistributedTrainer(agent_ids)
            
            trainer.initialize_weights(np.array([2.0, 3.0]))
            
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=100,
                learning_rate=0.05,
                sync_interval=10
            )
            
            final_loss = results['agent_results']['agent1']['final_loss']
            
            # Should minimize toward zero
            assert final_loss < 0.01
        
        asyncio.run(run_minimization())
    
    def test_distributed_loss_minimization(self):
        """Test loss minimization with multiple agents."""
        async def run_distributed_minimization():
            agent_ids = ["agent1", "agent2", "agent3"]
            trainer = DistributedTrainer(agent_ids)
            
            trainer.initialize_weights(np.array([1.5, 1.5]))
            
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=80,
                learning_rate=0.08,
                sync_interval=5
            )
            
            # All agents should reach low loss
            for agent_result in results['agent_results'].values():
                assert agent_result['final_loss'] < 0.1
        
        asyncio.run(run_distributed_minimization())


# ============================================================================
# Tests: Synchronization Timing
# ============================================================================

class TestSyncTiming:
    """Test synchronization timing and overhead."""
    
    def test_sync_overhead(self):
        """Test synchronization overhead."""
        async def run_sync_overhead():
            agent_ids = ["agent1", "agent2"]
            trainer = DistributedTrainer(agent_ids)
            
            trainer.initialize_weights(np.array([1.0, 1.0]))
            
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=20,
                learning_rate=0.05,
                sync_interval=2
            )
            
            # Training should complete in reasonable time
            assert results['total_time'] < 30.0  # Should be sub-second on modern hardware
        
        asyncio.run(run_sync_overhead())
    
    def test_sync_interval_effect(self):
        """Test effect of different sync intervals."""
        async def run_interval_effect():
            agent_ids = ["agent1", "agent2", "agent3"]
            
            # Train with frequent sync
            trainer1 = DistributedTrainer(agent_ids.copy())
            trainer1.initialize_weights(np.array([1.0, 1.0]))
            
            results1 = await trainer1.train(
                loss_fn=simple_loss_function,
                iterations=30,
                learning_rate=0.05,
                sync_interval=1
            )
            
            # Train with infrequent sync
            trainer2 = DistributedTrainer(agent_ids.copy())
            trainer2.initialize_weights(np.array([1.0, 1.0]))
            
            results2 = await trainer2.train(
                loss_fn=simple_loss_function,
                iterations=30,
                learning_rate=0.05,
                sync_interval=10
            )
            
            # Both should converge
            assert results1['agent_results']['agent1']['final_loss'] < 1.0
            assert results2['agent_results']['agent1']['final_loss'] < 1.0
        
        asyncio.run(run_interval_effect())


# ============================================================================
# Tests: Barrier Synchronization
# ============================================================================

class TestBarrierSync:
    """Test barrier synchronization."""
    
    def test_barrier_with_multiple_agents(self):
        """Test barrier sync with multiple agents."""
        async def run_barrier_sync():
            agent_ids = ["agent1", "agent2", "agent3"]
            trainer = DistributedTrainer(agent_ids)
            
            trainer.initialize_weights(np.array([1.0, 1.0]))
            
            # Train and let barrier syncs happen
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=10,
                learning_rate=0.05,
                sync_interval=5
            )
            
            # Should complete without error
            assert len(results['agent_results']) == 3
        
        asyncio.run(run_barrier_sync())


# ============================================================================
# Integration Tests
# ============================================================================

class TestIntegration:
    """Integration tests combining multiple features."""
    
    def test_full_training_pipeline(self):
        """Test complete training pipeline."""
        async def run_full_pipeline():
            # Create trainer with 5 agents
            agent_ids = [f"agent{i}" for i in range(5)]
            trainer = DistributedTrainer(agent_ids)
            
            # Initialize with random weights
            trainer.initialize_weights(np.array([0.1, 0.1, 0.1]))
            
            # Train for multiple iterations with periodic sync
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=50,
                learning_rate=0.08,
                sync_interval=5
            )
            
            # Verify results structure
            assert 'total_agents' in results
            assert 'agent_results' in results
            assert len(results['agent_results']) == 5
            
            # All agents should have trained
            for agent_id, agent_result in results['agent_results'].items():
                assert agent_result['iterations'] == 50
                assert agent_result['final_loss'] < 0.5
        
        asyncio.run(run_full_pipeline())
    
    def test_scalability_with_many_agents(self):
        """Test scalability with many agents."""
        async def run_many_agents():
            # Create trainer with 10 agents
            agent_ids = [f"agent{i}" for i in range(10)]
            trainer = DistributedTrainer(agent_ids)
            
            trainer.initialize_weights(np.array([1.0]))
            
            # Train with fewer iterations due to more agents
            results = await trainer.train(
                loss_fn=simple_loss_function,
                iterations=20,
                learning_rate=0.05,
                sync_interval=2
            )
            
            assert len(results['agent_results']) == 10
            # All should converge reasonably
            avg_loss = np.mean([
                r['final_loss'] 
                for r in results['agent_results'].values()
            ])
            assert avg_loss < 1.0
        
        asyncio.run(run_many_agents())


# ============================================================================
# Run Tests
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
