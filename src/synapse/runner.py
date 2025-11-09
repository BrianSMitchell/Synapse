import sys
from synapse.parser.parser import parse_and_execute

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'run':
        print("Usage: synapse run <file.syn>")
        sys.exit(1)

    file_path = sys.argv[2]
    try:
        with open(file_path, 'r') as f:
            code = f.read()
        result = parse_and_execute(code)
        if result is not None:
            print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
