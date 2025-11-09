import subprocess
import sys

# Simulate demo
commands = [
    "let x = normal(0,1)",
    "sample(x)",
    "let belief = bernoulli(0.7)",
    "if sample(belief) > 0.5 { 1 }",
    "exit"
]

print("Synapse REPL Demo")
print("==================")

for cmd in commands:
    print(f"synapse> {cmd}")
    if cmd == "exit":
        break
    # Simulate execution
    from synapse.parser.parser import parse_and_execute
    try:
        result = parse_and_execute(cmd)
        if result is not None:
            print(result)
    except Exception as e:
        print(f"Error: {e}")

print("Goodbye!")
