# Flask Test

## Initial steps

1. Install Flask: `sudo pip3 install Flask`
2. Create new file from which we will run the application. The convention is to use 'run.py' or 'app.py' 
3. In the newly created file add the following: `from flask import Flask` and `app = Flask(__name__)`
4. Then add a decorator `@app.route('/')` etc...


The decorator is used to link elements, for example two html pages. To achieve it, we need to do something called routing. You've already been introduced to routing in Flask because we used this decorator here, which we discussed before, and the "/". So when we go to the "/" on a top-level of our site, it then returns the template from our index() function. The root decorator binds the index() function to itself so that whenever that root is called, the function is called.



