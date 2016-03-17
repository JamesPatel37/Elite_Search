import hashlib

def hash_filepath(filepath):
    hasher = hashlib.md5(filepath)
    return hasher.hexdigest()