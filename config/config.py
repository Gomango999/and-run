config = {    
    # Compiler options - used when compiling code
    "compiler": "g++",
    "flags": "-std=c++14 -Wall -Wno-misleading-indentation -Wno-char-subscripts",
    # TODO: Add address sanitisation
    
    # The keywords used to match input, output and expected output files
    "input_key": "in",
    "output_key": "out",
    "expected_key": "out",
    # "expected_key": "ans",
    
    # Diff command - used when comparing output
    # "diff_command": "diff -yw {} {} | colordiff",
    "diff_command": "diff -yw {} {}",
    
    # Editor options - used when opening this file
    "editor_command": "subl",
    
    # Number of lines of input to display when running code
    "input_lines": 10,
}