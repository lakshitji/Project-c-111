import os
import shutil

from_dir = "Downloads"
to_dir = "/D"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

path = "Downloads/mushroom-house.jpg"
root,ext = os.path.splitext(path)
print("Root of the path:",root)
print("Extension of the path:",ext)