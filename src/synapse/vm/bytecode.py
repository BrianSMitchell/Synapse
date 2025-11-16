"""
Custom Bytecode VM for Synapse
Implements a register-based virtual machine with JIT support
"""

from typing import List, Dict, Any, Optional, Callable
from enum import Enum
from dataclasses import dataclass
import time


class Opcode(Enum):
    """VM Instruction opcodes"""
    # Constants and variables
    LOAD_CONST = 0x00
    LOAD_VAR = 0x01
    STORE_VAR = 0x02
    
    # Arithmetic
    ADD = 0x10
    SUB = 0x11
    MUL = 0x12
    DIV = 0x13
    MOD = 0x14
    NEG = 0x15
    
    # Comparison
    CMP_EQ = 0x20
    CMP_NE = 0x21
    CMP_LT = 0x22
    CMP_LE = 0x23
    CMP_GT = 0x24
    CMP_GE = 0x25
    
    # Logical
    AND = 0x30
    OR = 0x31
    NOT = 0x32
    
    # Control flow
    JUMP = 0x40
    JUMP_IF_FALSE = 0x41
    JUMP_IF_TRUE = 0x42
    
    # Functions
    CALL = 0x50
    RETURN = 0x51
    
    # Array operations
    LOAD_ARRAY = 0x60
    STORE_ARRAY = 0x61
    ARRAY_INDEX = 0x62
    ARRAY_LEN = 0x63
    
    # I/O
    PRINT = 0x70
    
    # Miscellaneous
    NOP = 0xFF


@dataclass
class Instruction:
    """Represents a VM instruction"""
    opcode: Opcode
    arg1: Optional[int] = None
    arg2: Optional[int] = None
    arg3: Optional[int] = None
    
    def __repr__(self):
        args = []
        if self.arg1 is not None:
            args.append(str(self.arg1))
        if self.arg2 is not None:
            args.append(str(self.arg2))
        if self.arg3 is not None:
            args.append(str(self.arg3))
        
        args_str = f" {', '.join(args)}" if args else ""
        return f"{self.opcode.name}{args_str}"


class CallFrame:
    """Represents a function call frame"""
    
    def __init__(self, name: str, ip: int, locals: Dict[str, Any]):
        self.name = name
        self.ip = ip  # Return instruction pointer
        self.locals = locals.copy()


class BytecodeVM:
    """Register-based Synapse VM"""
    
    def __init__(self, max_registers: int = 256):
        self.max_registers = max_registers
        self.registers: List[Any] = [None] * max_registers
        self.globals: Dict[str, Any] = {}
        self.call_stack: List[CallFrame] = []
        self.constants: List[Any] = []
        self.functions: Dict[str, Dict[str, Any]] = {}
        self.code: List[Instruction] = []
        self.ip = 0  # Instruction pointer
        self.sp = 0  # Stack pointer (register pointer)
        self.execution_time = 0.0
        self.instruction_count = 0
        self.jit_enabled = False
        self.jit_cache: Dict[int, Callable] = {}
        self.jit_threshold = 100  # JIT compile after 100 executions
    
    def load_bytecode(self, bytecode: List[Instruction]) -> None:
        """Load bytecode into VM"""
        self.code = bytecode
        self.ip = 0
    
    def load_constant(self, value: Any) -> int:
        """Add a constant and return its index"""
        self.constants.append(value)
        return len(self.constants) - 1
    
    def emit(self, opcode: Opcode, arg1: Optional[int] = None, 
             arg2: Optional[int] = None, arg3: Optional[int] = None) -> int:
        """Emit an instruction and return its index"""
        instr = Instruction(opcode, arg1, arg2, arg3)
        self.code.append(instr)
        return len(self.code) - 1
    
    def execute(self) -> Any:
        """Execute the loaded bytecode"""
        start_time = time.time()
        self.instruction_count = 0
        
        while self.ip < len(self.code):
            instr = self.code[self.ip]
            self.instruction_count += 1
            
            # Check if JIT should compile this hot path
            if self.jit_enabled and self.instruction_count % self.jit_threshold == 0:
                self._maybe_jit_compile(self.ip)
            
            # Execute instruction
            self._execute_instruction(instr)
            
            if self.ip < len(self.code):
                self.ip += 1
        
        self.execution_time = time.time() - start_time
        result = self.registers[0] if self.sp > 0 else None
        return result
    
    def _execute_instruction(self, instr: Instruction) -> None:
        """Execute a single instruction"""
        op = instr.opcode
        
        if op == Opcode.NOP:
            pass
        
        elif op == Opcode.LOAD_CONST:
            # Load constant into register
            const_idx = instr.arg1
            reg = instr.arg2 or self.sp
            self.registers[reg] = self.constants[const_idx]
            self.sp = max(self.sp, reg + 1)
        
        elif op == Opcode.LOAD_VAR:
            # Load variable into register
            var_name = self.constants[instr.arg1]
            reg = instr.arg2 or self.sp
            value = self.globals.get(var_name)
            if value is None and self.call_stack:
                value = self.call_stack[-1].locals.get(var_name)
            self.registers[reg] = value
            self.sp = max(self.sp, reg + 1)
        
        elif op == Opcode.STORE_VAR:
            # Store register into variable
            var_name = self.constants[instr.arg1]
            reg = instr.arg2 or self.sp - 1
            value = self.registers[reg]
            self.globals[var_name] = value
        
        elif op == Opcode.ADD:
            # Add two registers
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] + self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.SUB:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] - self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.MUL:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] * self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.DIV:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] / self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.MOD:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] % self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.NEG:
            reg, dest = instr.arg1, instr.arg2 or self.sp
            self.registers[dest] = -self.registers[reg]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.CMP_EQ:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] == self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.CMP_NE:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] != self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.CMP_LT:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] < self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.CMP_LE:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] <= self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.CMP_GT:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] > self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.CMP_GE:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] >= self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.AND:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] and self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.OR:
            reg1, reg2, dest = instr.arg1, instr.arg2, instr.arg3 or self.sp
            self.registers[dest] = self.registers[reg1] or self.registers[reg2]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.NOT:
            reg, dest = instr.arg1, instr.arg2 or self.sp
            self.registers[dest] = not self.registers[reg]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.JUMP:
            target = instr.arg1
            self.ip = target - 1  # -1 because ip will be incremented
        
        elif op == Opcode.JUMP_IF_FALSE:
            cond_reg = instr.arg1
            target = instr.arg2
            if not self.registers[cond_reg]:
                self.ip = target - 1
        
        elif op == Opcode.JUMP_IF_TRUE:
            cond_reg = instr.arg1
            target = instr.arg2
            if self.registers[cond_reg]:
                self.ip = target - 1
        
        elif op == Opcode.PRINT:
            # Print register contents
            reg = instr.arg1
            print(self.registers[reg])
        
        elif op == Opcode.ARRAY_INDEX:
            # Load array element
            array_reg = instr.arg1
            index_reg = instr.arg2
            dest = instr.arg3 or self.sp
            array = self.registers[array_reg]
            index = int(self.registers[index_reg])
            self.registers[dest] = array[index]
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.ARRAY_LEN:
            array_reg = instr.arg1
            dest = instr.arg2 or self.sp
            array = self.registers[array_reg]
            self.registers[dest] = len(array)
            self.sp = max(self.sp, dest + 1)
        
        elif op == Opcode.RETURN:
            # Return from function
            if self.call_stack:
                frame = self.call_stack.pop()
                self.ip = frame.ip - 1
    
    def _maybe_jit_compile(self, ip: int) -> None:
        """Consider JIT compiling a hot code path"""
        if ip not in self.jit_cache:
            # Simple JIT: pre-compile linear sequences
            self.jit_cache[ip] = self._compile_sequence(ip)
    
    def _compile_sequence(self, start_ip: int) -> Callable:
        """Compile a sequence of instructions into native Python"""
        def compiled_sequence():
            ip = start_ip
            while ip < len(self.code) and ip - start_ip < 10:
                instr = self.code[ip]
                self._execute_instruction(instr)
                ip += 1
            return self.registers[0]
        return compiled_sequence
    
    def disassemble(self) -> str:
        """Disassemble bytecode for debugging"""
        lines = []
        for i, instr in enumerate(self.code):
            lines.append(f"{i:3d}: {instr}")
        return '\n'.join(lines)
    
    def benchmark(self, iterations: int = 1000) -> Dict[str, float]:
        """Benchmark VM execution"""
        start = time.time()
        
        for _ in range(iterations):
            self.ip = 0
            self.sp = 0
            self.execute()
        
        total_time = time.time() - start
        
        return {
            'total_time': total_time,
            'avg_time_per_iteration': total_time / iterations,
            'iterations_per_second': iterations / total_time,
            'instructions_executed': self.instruction_count,
        }


class VMCompiler:
    """Compiles AST to bytecode"""
    
    def __init__(self):
        self.vm = BytecodeVM()
        self.var_counter = 0
    
    def compile(self, ast) -> BytecodeVM:
        """Compile AST to bytecode in VM"""
        self.vm.code = []
        self._compile_ast(ast)
        return self.vm
    
    def _compile_ast(self, ast) -> int:
        """Compile AST node and return register for result"""
        # This is a placeholder; actual implementation would recursively
        # compile the AST from the self_host module
        return 0
    
    def allocate_register(self) -> int:
        """Allocate a new register"""
        reg = self.var_counter
        self.var_counter += 1
        return reg


def test_bytecode_vm():
    """Test bytecode VM execution"""
    vm = BytecodeVM()
    
    # Compile: let x = 42, y = 10, z = x + y
    const_42 = vm.load_constant(42)
    const_10 = vm.load_constant(10)
    
    # Load 42 into register 0
    vm.emit(Opcode.LOAD_CONST, const_42, 0)
    
    # Load 10 into register 1
    vm.emit(Opcode.LOAD_CONST, const_10, 1)
    
    # Add registers 0 and 1, store in register 2
    vm.emit(Opcode.ADD, 0, 1, 2)
    
    # Print register 2
    vm.emit(Opcode.PRINT, 2)
    
    print("Bytecode:")
    print(vm.disassemble())
    
    print("\nExecution:")
    result = vm.execute()
    print(f"Result: {result}")
    print(f"Execution time: {vm.execution_time * 1000:.2f}ms")
    
    # Benchmark
    print("\nBenchmark (1000 iterations):")
    bench = vm.benchmark(1000)
    for key, value in bench.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    test_bytecode_vm()
