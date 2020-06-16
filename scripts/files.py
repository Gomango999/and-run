# Holds scripts pertaining to finding finding cpp and input files.
import os

# Returns the number of lines of a file
def file_len(filename):
    i = 0
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Returns the first n lines of a file.
# Requires that the file has at least n lines
def file_head(filename, n):
    with open(filename) as f:
        assert(len(f.readlines()) >= n)
        return "".join(f.readlines()[0:n])


# Checks to see if filename is an input file
# An input file is:
#   - A .txt file ending in 'in.txt',
#   - A .txt file with input in its name, or
#   - A .in file
def is_input_filename(filename):
    fileroot, file_extension = os.path.splitext(filename)
    fileroot = fileroot.lower()
    if ".txt" == file_extension:
        if "in" == fileroot[-2:]:
            return True
        elif "input" in fileroot:
            return True
    elif ".in" == file_extension:
        return True
    return False

# Checkts to see if filename is an input file
# An input file is:
#   - A .txt file ending in 'in.txt',
#   - A .txt file with input in its name, or
#   - A .in file
def is_output_filename(filename):
    fileroot, file_extension = os.path.splitext(filename)
    fileroot = fileroot.lower()
    if ".txt" == file_extension:
        if "out" == fileroot[-3:]:
            return True
        elif "output" in fileroot:
            return True
    elif ".out" == file_extension:
        return True
    return False

# Automatically selects the file that is most likely the input file
def get_input_filename():
    input_filenames = []
    for filename in os.listdir(os.getcwd()):
        if is_input_filename(filename):
            input_filenames.append(filename)
    if len(input_filenames) == 0:
        return None
    input_filenames.sort()
    return input_filenames[0]

# Automatically selects the file that is most likely the output file
def get_output_filename():
    output_filenames = []
    for filename in os.listdir(os.getcwd()):
        if is_output_filename(filename):
            output_filenames.append(filename)
    if len(output_filenames) == 0:
        return None
    output_filenames.sort()
    return output_filenames[0]

# Selects the most likely cpp file to be used
# A cpp file
#   - ends in .cpp, and
#   - does not contain test in its name
# TODO: Make it more likely to match with files that match the folder name
def get_cpp_filename():
    cwd = os.getcwd()
    cpp_filenames = []
    for f in os.listdir(cwd):
        filename, file_extension = os.path.splitext(f)
        # Find cpp file
        if ".cpp" == file_extension:
            if "test" in f.lower():
                continue
            cpp_filenames.append(f)
    cpp_filenames.sort()

    if len(cpp_filenames) == 0:
        return None
    return cpp_filenames[0]

# Returns the current basename
def get_basename():
    cwd = os.getcwd()
    return os.path.basename(os.path.normpath(os.getcwd()))
