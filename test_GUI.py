from flask import Flask
from home import *

app = Flask(__name__)

#connet a webpage
# froward slash means root directory
# give path in following argument of route method
@app.route('/')
def index():
    return "This is awesome."

@app.route('/about')
def about():
    return "this is about"
@app.route('/search/<searchQuery>')
def search(searchQuery):
    make_hash_link()
    results = print_updated_json(searchQuery)
    print len(results)
    final_result = []
    for each_value in results:
        each_value = str(each_value).replace("\\","//")
        final_result.append("<a target='_blank' href='file:///"+str(each_value)+"'>"+str(each_value)+"</a><br>")
    return str(final_result)

@app.route('/profile/<username>')
def profile(username):
    return "hey there %s" % username

@app.route('/post/<int:post_id>')
def show(post_id):
    return "post id is %s" % post_id

if __name__ == "__main__":
    app.run(debug=True)