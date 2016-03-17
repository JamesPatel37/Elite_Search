from variables import *
import json

def json_word_hash():
    with open('word_hash.json', mode='w+') as f:
        json.dump(word_hash, f)