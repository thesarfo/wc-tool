import argparse
import sys
import os

if __name__ == "__main__":
	file_option = "filename"
	is_tty = sys.stdin.isatty() 
	if not is_tty:
		file_option = "--filename"
	parser = argparse.ArgumentParser(prog="wc", description="same functionality as wc in the linux cli")
	parser.add_argument(file_option)
	parser.add_argument("-c", "--count", action="store_true")
	parser.add_argument("-l", "--line-count", action="store_true")
	parser.add_argument("-w", "--words", action="store_true")
	parser.add_argument("-m", "--word-count", action="store_true")

	args = parser.parse_args()

	content = None
	if is_tty:
		_, filename = os.path.split(args.filename)
		with open(args.filename, "rb") as file:
			content = file.read()
		no_args = len(sys.argv) <= 2
	else:
		filename = ""
		content = sys.stdin.buffer.read()
		no_args = len(sys.argv) <= 1
	
	count, line_count, words = 0, 0, 0
	
	if args.count or no_args or not is_tty:
		count = len(content)
		if args.count: 
			(not no_args or is_tty) and print(count, filename)
	
	if args.line_count or no_args or not is_tty:
		for char in content.decode("utf-8"):
			if char == "\n":
				line_count += 1
		if args.line_count: 
			(not no_args or is_tty) and print(line_count, filename)
	
	if args.words or no_args or not is_tty:
		words = len(content.decode("utf-8").split()) 
		if args.words:
			(not no_args or is_tty) and print(words, filename)

	if args.word_count or not is_tty:
		if args.word_count:
			print(len(content.decode("utf-8")), filename)
	
	if no_args:
		print(line_count, words, count, filename)