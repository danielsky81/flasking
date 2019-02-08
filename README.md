# Flask Test

## Initial steps

1. Install Flask: `sudo pip3 install Flask`
2. Create new file from which we will run the application. The convention is to use 'run.py' or 'app.py' 
3. In the newly created file add the following: `from flask import flask` and `app = Flask(__name__)`
4. Then add a decorator `@app.route('/')` etc...