import sys
from synapse.parser.parser import parse_and_execute

def main():
    print("Synapse REPL - A Language for Emergent Intelligence")
    print("Type 'exit' to quit.")
    while True:
        try:
            line = input("synapse> ")
            if line.strip() == "exit":
                break
            result = parse_and_execute(line)
            if result is not None:
                print(result)
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")
    print("Goodbye!")

if __name__ == "__main__":
    main()
