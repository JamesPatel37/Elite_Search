from flask import Flask
from flask import request
from search import *
import time

app = Flask(__name__)

@app.route('/')
def index():
    home_html = """
    <html>
    <head>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
    </head>
    <body class='container'>
    <div class='col-lg-12' style='margin-top:20%'>
        <form action="/search_results" method="POST">
        Search Term: <input type="text" name="myform"><br>
        <input class='btn btn-primary' type="submit" value="Submit" text='Search'>
        </form>
    </div>
    </body>
    </html>"""
    return home_html

def search_json(search_term):
    file_content = open('word_hash.json', mode='r')
    json_content = json.loads(file_content.read())
    results = []
    for each_object in json_content:
        if search_term in each_object:
            the_hash = json_content[each_object]
            results.append(the_hash)
            print str(each_object)+":"+str(json_content[each_object])
    return results
@app.route('/search_results', methods=['POST'])
def search_results():

    search_term = request.form['myform']

    process_hash = {}

    the_flag = 1
    if the_flag == 0:
        results = search_json(search_term)
    else:
        results = search(search_term)

    for each_item in results:
        for each_value in each_item:
            process_hash[each_value] = each_item[each_value]

    display_hash=[]

    display_hash_view = [ (v,k) for k,v in process_hash.iteritems() ]
    display_hash_view.sort(reverse=True)

    for v,k in display_hash_view:
        display_hash.append(str(filename_hash_list[k])+", Rank :"+str(v))

    display_html = ""

    for each_value in display_hash:
        hyperlink = each_value.split(',')
        display_html += "<a target='_blank' href='file:///"+str(hyperlink[0])+"'>"+str(each_value)+"</a><br>"
    display_html += "</body>"
    display_html += "</html>"

    return display_html

if __name__ == "__main__":
    app.run(debug=True)