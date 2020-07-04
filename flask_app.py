
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
#Webhook into Git to get the latest code
import git
app = Flask(__name__)
@app.route('/', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('path/to/git_repo')
            origin = repo.remotes.origin
origin.pull()
return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400
app = Flask(__name__)
#End of webhook


@app.route('/home')
def hello_world():
    return 'Hello from Flask!'
