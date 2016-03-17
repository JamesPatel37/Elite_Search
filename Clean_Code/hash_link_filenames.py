from variables import *
import os
from hash_filepath import *

def hash_link_filenames():

    global total_files

    for root, dirs, files in os.walk(mainDirectory):
        for each_filename in files:
            filename = str(each_filename)
            file_path = os.path.realpath(os.path.join(root, filename))
            hash_value = hash_filepath(file_path)
            filename_hash_list[hash_value] = file_path

            total_files+=1
            print "Hashing : "+str(total_files)
from variables import *
import json

def json_word_hash():
    with open('filename_hash.json', mode='w+') as f:
        json.dump(filename_hash_list, f)
