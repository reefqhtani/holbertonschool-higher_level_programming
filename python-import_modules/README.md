Python - Import & Modules
https://img.shields.io/badge/python-3.8-blue.svg

This project introduces Python's module system and import functionality. Learn how to organize code across multiple files and import functions/variables between modules.

Project Overview
Master Python's import system, module creation, and command-line argument handling through practical exercises.

Learning Objectives
Import functions from other files

Create and use modules

Use the dir() built-in function

Prevent code execution when imported

Handle command line arguments

Work with Python's import system

Requirements
Python 3.8

Ubuntu 20.04 LTS

pycodestyle (version 2.7.*)

All files must be executable

Project Tasks
0. Import a simple function from a simple file
Import add function and print 1 + 2 = 3

1. My first toolbox!
Import calculator functions and perform basic operations

2. How to make a script dynamic!
Handle command line arguments with sys.argv

3. Infinite addition
Add all command line arguments

4. Who are you?
Discover and print names defined in hidden module

5. Everything can be imported
Import and print a variable from another module

Usage
bash
# Make executable and run
chmod +x filename.py
./filename.py

# Check code style
pycodestyle filename.py
File Structure
text
python-import_modules/
├── 0-add.py
├── 1-calculation.py
├── 2-args.py
├── 3-infinite_add.py
├── 4-hidden_discovery.py
├── 5-variable_load.py
└── README.md
Examples
python
# Import specific function
from module import function

# Import entire module
import module

# Prevent execution when imported
if __name__ == "__main__":
    # Your code here
Author
Holberton School
