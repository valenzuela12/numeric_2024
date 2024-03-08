"""
define the path to important folders without having
to install anything -- just do:

import context

then the path for the data directory is

context.data_dir

"""
import sys
from pathlib import Path

path = Path(__file__).resolve()  # this file
this_dir = path.parent  # this folder
lab_dir = this_dir
root_dir = lab_dir.parents[1]
data_dir = root_dir / Path("data")

print(lab_dir)
sys.path.insert(0,str(root_dir))
sep = "*" * 30
print(f"{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n"
      f"back of path: {sys.path[-1]}\n{sep}\n")


print(f"through {__file__}")
