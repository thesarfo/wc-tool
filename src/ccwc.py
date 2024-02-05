import sys
import locale

def print_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            bytes = len(file.read())
            return bytes
    except FileNotFoundError:
        print(f"Error: File '{filename}' cannot be found.")
        return 0

def print_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = sum(1 for line in file)
            return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

def print_words(filename):
    try:
        with open(filename, 'r') as file:
            words = sum(len(line.split()) for line in file)
            return words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

def print_characters(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            characters = len(file.read())
            return chars
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Correct usage is: ccwc  -c|-l|-w|-m <filename>")
        sys.exit(1)

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        bytes = print_bytes(filename)
        lines = print_lines(filename)
        words = print_words(filename)
        print(f"{lines: >6} {words: >7} {bytes: >7} {filename}")
        sys.exit(0)

    alt = sys.argv[1]
    filename = sys.argv[2]

    if alt == "-c":
        print(print_bytes(filename), filename)
    elif alt == "-l":
        print(print_lines(filename), filename)
    elif alt == "-w":
        print(print_words(filename), filename)
    elif alt == "-m":
        if locale.getpreferredencoding() == 'UTF-8':
            print(print_characters(filename), filename)
        else:
            print(print_bytes(filename), filename)
    else:
        bytes = print_bytes(filename)
        lines = print_lines(filename)
        words = print_words(filename)
        print(f"{lines: >6} {words: >7} {bytes: >7} {filename}")