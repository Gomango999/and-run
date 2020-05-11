# Holds scripts pertaining to finding finding cpp and input files.
import os

# Returns the number of lines of a file
def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Returns the first n lines of a file.
def file_head(filename, n):
    with open(filename) as f:
        return "".join(f.readlines()[0:n])

# Automatically selects the file that is most likely the input file
# An input file is:
#   - A .txt file ending in 'in.txt',
#   - A .txt file with input in its name, or
#   - A .in file
def get_input_file():
    cwd = os.getcwd()
    input_files = []
    for f in os.listdir(cwd):
        fileroot, file_extension = os.path.splitext(f)
        fileroot = fileroot.lower()

        # Find default input file
        if ".txt" == file_extension:
            if "in" == fileroot[-2:]:
                input_files.append(f)
            elif "input" in fileroot:
                input_files.append(f)
        elif ".in" == file_extension:
            input_files.append(f)

    input_files.sort()

    if len(input_files) == 0:
        return None
    return input_files[0]

# Selects the most likely cpp file to be used
# A cpp file
#   - ends in .cpp, and
#   - does not contain test in its name
# TODO: Make it more likely to match with files that match the folder name
def get_cpp_file():
    cwd = os.getcwd()
    cpp_files = []
    for f in os.listdir(cwd):
        filename, file_extension = os.path.splitext(f)
        # Find cpp file
        if ".cpp" == file_extension:
            if "test" in f.lower():
                continue
            cpp_files.append(f)
    cpp_files.sort()

    if len(cpp_files) == 0:
        return None
    return cpp_files[0]

# Returns the current basename
def get_basename():
    cwd = os.getcwd()
    return os.path.basename(os.path.normpath(cwd))
