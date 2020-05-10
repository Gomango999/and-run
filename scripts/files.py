import os

# Holds scripts pertaining to finding finding cpp and input files.
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def file_head(fname, num):
    with open(fname) as f:
        return "".join(f.readlines()[0:num])

# Selects an input file to be used
# If multiple, selects the first one
def get_input_file():
    cwd = os.getcwd()
    input_files = []
    for f in os.listdir(cwd):
        filename, file_extension = os.path.splitext(f)
        # Find default input file
        if ".txt" == file_extension:
            if "in" == filename.lower()[-2:]:
                input_files.append(f)
            elif "input" in filename:
                input_files.append(f)
        elif ".in" == file_extension:
            input_files.append(f)
    input_files.sort()

    if len(input_files) == 0:
        return None
    return input_files[0]

# Selects a cpp file to be used
# If multiple, selects the first one
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

def get_basename():
    cwd = os.getcwd()
    return os.path.basename(os.path.normpath(cwd))
