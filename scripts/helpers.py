from scripts.files import get_root_dir

# List of ANSI Escape codes for color
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
GRAY = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CURSOR_UP = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def print_fancy_bar(str):
    print(f"--------[{str}]--------")
    
root = get_root_dir()
template_paths = {
    "standard": root + f"/config/templates/standard.cpp",
    "cases":    root + f"/config/templates/cases.cpp",
    "light":    root + f"/config/templates/light.cpp",
    "empty":    root + f"/config/templates/empty.cpp",
} 
# NOTE: we maintain a special empty template that the user can not access
# normally. This will be used to check whether our file can be replaced or
# not when initialising cpp files (see `init.py`)