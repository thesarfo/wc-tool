import sys

def print_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            bytes = len(file.read())
            print(f"{bytes} {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' cannot be found.")

def print_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"{line_count} {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ["-c", "-l"]:
        print("Correct usage is: ccwc -c|-l <filename>")
        sys.exit(1)
    
    alt = sys.argv[1]
    filename = sys.argv[2]

    if alt == "-c":
        print_bytes(filename)
    elif alt == "-l":
        print_lines(filename)
