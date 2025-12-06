#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

# Test with "Holberton School"
import io
import sys

# Capture output
old_stdout = sys.stdout
sys.stdout = io.StringIO()

text_indentation("Holberton School")

output = sys.stdout.getvalue()
sys.stdout = old_stdout

print(f"Output: {repr(output)}")
print(f"Length: {len(output)}")
print(f"Expected: 'Holberton School\\n'")
print(f"Expected length: {len('Holberton School\\n')}")
