import sys

def print_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            bytes = len(file.read())
            print(f"{bytes} {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' cannot be found.")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "-c":
        print("Correct usage is: ccwc -c <filename>")
        sys.exit(1)
    
    filename = sys.argv[2]
    print_bytes(filename)