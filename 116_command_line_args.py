# Command Line Arguments Example
import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple greeting script.")
    parser.add_argument("name", help="The name to greet")
    parser.add_argument("-g", "--greeting", default="Hello", help="Greeting prefix")
    
    # We use a dummy list for demonstration instead of sys.argv
    args = parser.parse_args(["World", "--greeting", "Hi"])
    
    print(f"{args.greeting}, {args.name}!")

if __name__ == "__main__":
    main()
