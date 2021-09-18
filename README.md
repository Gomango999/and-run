# And Run
And Run is a CLI tool that aids in speeding up the repetitive tasks in competitive programming, aimed to be both efficient and convenient to use. The overall goal is for this tool to assist in contest management, compilation and running, and debugging of code in competive scenarios.

And Run is a personal tool, and is still under development.

## Usage
```sh
and run
```
Automatically finds the cpp file, as well as any input and output files if any, and then prints out the result of the program. It will print the input and output side by side for easy comparison.
```sh
and initletters [A|B|C|...|Z]
```
Generates folders from A to any letter.
```sh
and init -[standard|cases]
```
Generates a template cpp file. All templates include define macros and typedefs. Standard just has a main function, whereas cases also includes support by running the program repeatedly on multiple tests.


## Upcoming features
- Compiling and Running Code
    - Automatic compilation of all cpp files in a folder
- Faster Debugging
    - Tools to help find discrepant outputs based on a brute force solution and a random input generator
    - Tools to help find incorrect inputs based on a checker algorithm and a random input generator
- Generating Contest Workspaces
    - Automatic generation of multiple folders and code templates
    - Easier navigation of problems
    - Time tracking of problem completion for post contest analysis ?


## Technologies
And Run was coded in Python3 using the Click library. It is aimed at competitive programming in C++.
