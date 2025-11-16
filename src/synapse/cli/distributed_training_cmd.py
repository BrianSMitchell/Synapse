"""Synapse CLI Command for Distributed Agent Training

Provides CLI interface for distributed training operations:
- synapse train --agents=5 --iterations=100 --backend=local
- synapse train --agents=100 --backend=mpi --sync-interval=10
- synapse train --agents=1000 --backend=spark --master=spark://host:7077
"""

import argparse
import asyncio
import numpy as np
import json
from typing import Optional, List
from pathlib import Path

from synapse.core.distributed_training import (
    DistributedTrainer,
    MPIDistributedTrainer,
    SparkDistributedTrainer,
    simple_loss_function,
    ackley_loss_function,
)


class DistributedTrainingCommand:
    """Handle distributed training CLI commands."""
    
    def __init__(self):
        """Initialize command handler."""
        self.trainer = None
        self.results = None
    
    def add_parser(self, subparsers) -> argparse.ArgumentParser:
        """Add distributed training subcommand to parser.
        
        Args:
            subparsers: argparse subparsers group
            
        Returns:
            Configured argument parser
        """
        parser = subparsers.add_parser(
            'train',
            help='Distributed agent training'
        )
        
        parser.add_argument(
            '--agents', '-n',
            type=int,
            default=5,
            help='Number of agents (default: 5)'
        )
        
        parser.add_argument(
            '--iterations', '-i',
            type=int,
            default=100,
            help='Training iterations (default: 100)'
        )
        
        parser.add_argument(
            '--learning-rate', '-lr',
            type=float,
            default=0.05,
            help='Learning rate (default: 0.05)'
        )
        
        parser.add_argument(
            '--sync-interval', '-s',
            type=int,
            default=10,
            help='Synchronize every N iterations (default: 10)'
        )
        
        parser.add_argument(
            '--weights',
            type=float,
            nargs='+',
            default=[1.0, 1.0],
            help='Initial weights (default: 1.0 1.0)'
        )
        
        parser.add_argument(
            '--loss-function',
            choices=['simple', 'ackley'],
            default='simple',
            help='Loss function to optimize (default: simple)'
        )
        
        parser.add_argument(
            '--backend',
            choices=['local', 'mpi', 'spark'],
            default='local',
            help='Training backend (default: local)'
        )
        
        parser.add_argument(
            '--spark-master',
            type=str,
            default='local[*]',
            help='Spark master URL (default: local[*])'
        )
        
        parser.add_argument(
            '--output', '-o',
            type=str,
            help='Output file for results (JSON)'
        )
        
        parser.add_argument(
            '--verbose', '-v',
            action='store_true',
            help='Verbose output'
        )
        
        parser.set_defaults(func=self.execute)
        
        return parser
    
    async def execute(self, args: argparse.Namespace) -> int:
        """Execute distributed training command.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code (0 for success)
        """
        try:
            # Select loss function
            if args.loss_function == 'ackley':
                loss_fn = ackley_loss_function
            else:
                loss_fn = simple_loss_function
            
            # Create trainer based on backend
            if args.verbose:
                print(f"Creating {args.backend} trainer with {args.agents} agents...")
            
            agent_ids = [f"agent{i}" for i in range(args.agents)]
            
            if args.backend == 'mpi':
                try:
                    self.trainer = MPIDistributedTrainer(agent_ids)
                except ImportError:
                    print("Error: mpi4py is required for MPI backend")
                    print("Install with: pip install mpi4py")
                    return 1
            elif args.backend == 'spark':
                try:
                    self.trainer = SparkDistributedTrainer(
                        agent_ids,
                        spark_master=args.spark_master
                    )
                except ImportError:
                    print("Error: pyspark is required for Spark backend")
                    print("Install with: pip install pyspark")
                    return 1
            else:
                self.trainer = DistributedTrainer(agent_ids)
            
            # Initialize weights
            initial_weights = np.array(args.weights)
            if args.verbose:
                print(f"Initializing weights: {initial_weights}")
            
            self.trainer.initialize_weights(initial_weights)
            
            # Train
            if args.verbose:
                print(
                    f"Training {args.agents} agents for {args.iterations} iterations "
                    f"(sync every {args.sync_interval})"
                )
            
            self.results = await self.trainer.train(
                loss_fn=loss_fn,
                iterations=args.iterations,
                learning_rate=args.learning_rate,
                sync_interval=args.sync_interval
            )
            
            # Display results
            self._display_results(args)
            
            # Save results if requested
            if args.output:
                self._save_results(args.output)
                if args.verbose:
                    print(f"Results saved to: {args.output}")
            
            return 0
        
        except Exception as e:
            print(f"Error: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            return 1
        
        finally:
            # Cleanup
            if isinstance(self.trainer, SparkDistributedTrainer):
                self.trainer.stop()
    
    def _display_results(self, args: argparse.Namespace):
        """Display training results.
        
        Args:
            args: Command arguments
        """
        if not self.results:
            return
        
        print("\n" + "="*70)
        print("DISTRIBUTED TRAINING RESULTS")
        print("="*70)
        
        print(f"\nConfiguration:")
        print(f"  Backend:        {args.backend}")
        print(f"  Agents:         {self.results.get('total_agents', 'N/A')}")
        print(f"  Iterations:     {self.results.get('total_iterations', 'N/A')}")
        print(f"  Sync Interval:  {self.results.get('sync_interval', 'N/A')}")
        print(f"  Loss Function:  {args.loss_function}")
        
        print(f"\nPerformance:")
        total_time = self.results.get('total_time', 0)
        print(f"  Total Time:     {total_time:.2f}s")
        
        num_agents = self.results.get('total_agents', 0)
        if num_agents > 0 and total_time > 0:
            print(f"  Time/Agent:     {total_time/num_agents:.3f}s")
        
        print(f"\nAgent Results:")
        agent_results = self.results.get('agent_results', {})
        
        if agent_results:
            # Summary statistics
            final_losses = [
                r.get('final_loss', float('inf'))
                for r in agent_results.values()
            ]
            
            if final_losses:
                avg_loss = np.mean(final_losses)
                min_loss = np.min(final_losses)
                max_loss = np.max(final_losses)
                
                print(f"  Final Loss (Avg): {avg_loss:.6f}")
                print(f"  Final Loss (Min): {min_loss:.6f}")
                print(f"  Final Loss (Max): {max_loss:.6f}")
        
        print(f"\nAgent-by-Agent Breakdown:")
        for agent_id, result in sorted(agent_results.items())[:5]:
            print(f"  {agent_id}:")
            print(f"    Final Loss:     {result.get('final_loss', 'N/A'):.6f}")
            print(f"    Iterations:     {result.get('iterations', 'N/A')}")
            print(f"    Syncs:          {result.get('total_syncs', 'N/A')}")
            if result.get('avg_sync_time', 0) > 0:
                print(f"    Avg Sync Time:  {result.get('avg_sync_time', 0):.4f}s")
        
        if len(agent_results) > 5:
            print(f"  ... and {len(agent_results) - 5} more agents")
        
        print("="*70 + "\n")
    
    def _save_results(self, output_path: str):
        """Save results to JSON file.
        
        Args:
            output_path: Path to output file
        """
        if not self.results:
            return
        
        # Convert numpy types to native Python types
        def convert_types(obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, (np.integer, np.floating)):
                return obj.item()
            elif isinstance(obj, dict):
                return {k: convert_types(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_types(v) for v in obj]
            return obj
        
        results_json = convert_types(self.results)
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(results_json, f, indent=2)


def register_command(parser: argparse.ArgumentParser) -> None:
    """Register distributed training command with CLI.
    
    Args:
        parser: Main argument parser
    """
    subparsers = parser.add_subparsers(dest='subcommand', help='Subcommands')
    command = DistributedTrainingCommand()
    command.add_parser(subparsers)


# For direct invocation
if __name__ == '__main__':
    import sys
    
    parser = argparse.ArgumentParser(
        prog='synapse train',
        description='Synapse distributed agent training'
    )
    
    command = DistributedTrainingCommand()
    command.add_parser(parser._subparsers._group_actions[0].choices)
    
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        exit_code = asyncio.run(args.func(args))
        sys.exit(exit_code)
    else:
        parser.print_help()
        sys.exit(0)
