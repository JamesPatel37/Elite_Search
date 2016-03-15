#import statements
import os
from hash_file import *



#variables
mainDirectory = 'F:\\CS454-Python\\en';  # root path
filename_hash_list = {}

#methods
def hash_link():
    for root, dirs, files in os.walk(mainDirectory):
        for each_filename in files:
            filename = str(each_filename)
            file_path = os.path.realpath(os.path.join(root, filename))
            hash_value = hash_filepath(file_path)
            filename_hash_list[hash_value] = file_path
            print hash_value +":"+file_path
def read_file(file_path):
    for each_value in filename_hash_list:
        