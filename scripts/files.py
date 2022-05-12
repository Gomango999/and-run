# Scripts to help with finding and managing files
import os
import re

from config.config import config

def get_file_len(filename):
    """ Returns the number of lines of a file
    """
    with open(filename) as f:
        x = len(f.readlines())
    return x

def get_root_dir():
    """ Returns the root directory where this python script is hosted
    """
    root = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    return root

def get_basename():
    """ Gets the name of the folder containing the current file
    """
    return os.path.basename(os.path.normpath(os.getcwd()))

def get_sorting_string(filename, key):
    """ Move the number between "{key}" and ".txt" to the front, followed by the name
        - E.g. beachin5.txt becomes 0000000005beachin
        - E.g. in3.txt becomes 0000000003in
        - E.g. beach5.in becomes 0000000005beach
        - Used in sorting inputs in order
    """
    if re.search(f"{key}\d*\.txt$", filename): # e.g. in3.txt
    
        # find the match
        match = re.findall(f"{key}\d*\.txt$", filename)
        assert(len(match) == 1)
        match = match[0]
        
        # get the number and left pad it with 0 
        digit_start = -len(match)+len(key)
        digit_end = -4 
        number = match[digit_start:digit_end].zfill(10) 
        
        # append the base file name onto the end
        base_name = filename[:-len(match)] 
        s = number + base_name
        
    elif re.search(f"\d*.{key}$", filename): # e.g. something3.in
    
        # find the match
        match = re.findall(f"\d*.{key}$", filename)
        assert(len(match) == 1)
        match = match[0]
        
        # get the number and left pad it with 0
        digit_start = -len(match)
        digit_end = -len(key) - 1 
        number = match[digit_start:digit_end].zfill(10) 
        
        # append the base file name onto the end
        base_name = filename[:-len(match)] 
        s = number + base_name
    
    return s
    
def find_filenames_with_key(key):
    """ Returns a sorted list of files ending with {key}.txt or .{key}
    """
    filenames = []
    for filename in os.listdir(os.getcwd()):
        if re.search(f"{key}\d*\.txt$", filename): # e.g. in3.txt
            filenames.append(filename)
        elif re.search(f"\d*.{key}$", filename): # e.g. something3.in
            filenames.append(filename)
    
    # Sort filenames by their number
    filenames.sort(key=lambda x : get_sorting_string(x, key))
    
    return filenames
    
def get_input_filenames():
    """ Returns a sorted list of input files in the current directory
        - Input files must end in in.txt, in<number>.txt, or .in
        - E.g. in.txt, beachin3.txt, cat.in
    """
    return find_filenames_with_key(config["input_key"])
    
def get_output_filenames():
    """ Returns a sorted list of output files in the current directory
        - Input files must end in out.txt, out<number>.txt, or .out
        - E.g. out.txt, beachout3.txt, cat.out
    """
    return find_filenames_with_key(config["output_key"])
    
def get_expected_filenames():
    """ Returns a sorted list of expected files in the current directory
        - Input files must end in ans.txt, ans<number>.txt, or .ans
        - E.g. ans.txt, beachans3.txt, cat.ans
    """
    return find_filenames_with_key(config["expected_key"])

def replace_key(filename, key1, key2):
    """ Replaces the key1 with key2 with another one
        - E.g. in.txt becomes out.txt
    """
    if re.search(f"{key1}\d*\.txt$", filename): # e.g. in3.txt
    
        # find the match and replace
        match = re.findall(f"{key1}\d*\.txt$", filename)
        assert(len(match) == 1)
        match = match[0]

        base_name = filename[:-len(match)] 
        return base_name + match.replace(key1, key2)
        
    elif re.search(f"\d*.{key1}$", filename): # e.g. something3.in
    
        # find the match and replace
        match = re.findall(f"\d*.{key1}$", filename)
        assert(len(match) == 1)
        match = match[0]

        base_name = filename[:-len(match)] 
        return base_name + match.replace(key1, key2)

def inputfile_to_outputfile(input_filename):
    """ Gets the corresponding output file for an input file by replacement
    """
    return replace_key(input_filename, config["input_key"], config["output_key"])
    
def inputfile_to_expectedfile(input_filename):
    """ Gets the corresponding expected output file for an input file by replacement
    """
    return replace_key(input_filename, config["input_key"], config["expected_key"])