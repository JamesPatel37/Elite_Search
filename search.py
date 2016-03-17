from variables import *
from json_write import *
from hash_link_filenames import *
from crawl import *

def search(search_query):

    hash_link_filenames()

    crawl()

    json_word_hash()

    return_result_list = []

    for each_word in word_hash:
        if search_query in each_word:
            result_list = word_hash[each_word]
            return_result_list.append(result_list)
    return return_result_list
