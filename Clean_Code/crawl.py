from variables import *
from bs4 import BeautifulSoup

def crawl():

    file_count = 0
    global total_files
    for each_hash in filename_hash_list:

        file_count+=1
        print "Processing : "+str(file_count)

        file_path = filename_hash_list[each_hash]
        file_content = open(file_path, mode='r')
        soup = BeautifulSoup(file_content, 'html.parser')#feed to Beautifulsoup
        text_content_from_file = soup.get_text()
        split_text =  text_content_from_file.split()
        for each_word in split_text:
            each_word_freq = split_text.count(each_word)
            if each_word in word_hash:
                counter_hash = word_hash[each_word]
                if not each_hash in counter_hash:
                    counter_hash[each_hash] = each_word_freq
            else:
                word_hash[each_word] = {}
                counter_hash = word_hash[each_word]
                counter_hash[each_hash] = each_word_freq