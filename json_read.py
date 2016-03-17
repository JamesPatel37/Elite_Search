import json
import time
file_content = open('word_hash.json', mode='r')
json_content = json.loads(file_content.read())
for each_object in json_content:
    time.sleep(2)
    print str(each_object)+":"+str(json_content[each_object])