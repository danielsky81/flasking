# Flask Test

Small project to test a Flask framework.

Project is deployed to [Heroku](https://www.heroku.com/) and can be viewed [here](https://surfing-legends.herokuapp.com/).

## Initial steps

1. Install Flask: `sudo pip3 install Flask`
2. Create new file from which we will run the application. The convention is to use 'run.py' or 'app.py' 
3. In the newly created file add the following: `from flask import Flask` and `app = Flask(__name__)`
4. Then add a decorator `@app.route('/')` etc...


The decorator is used to link elements, for example two html pages. To achieve it, we need to do something called routing. You've already been introduced to routing in Flask because we used this decorator here, which we discussed before, and the "/". So when we go to the "/" on a top-level of our site, it then returns the template from our index() function. The root decorator binds the index() function to itself so that whenever that root is called, the function is called.

## Deployement

- One of many steps required are as follows:
    - Add "requirements.txt" file
    - Add "Procfile" via CLI `$ echo web: python run.py > Procfile`
- To avoid the error in deployment a web process needs to be started via `$ heroku ps:scale web=1`
- Then, we need to set the `IP` and `PORT` variables.
- Finally "Restart all dynos" so restarting to container of the website.

# Resources & Credits

- [Wikipedia](https://en.wikipedia.org/wiki/Main_Page).
- [Stadiumtalk's](https://www.stadiumtalk.com/s/30-greatest-surfers-all-time-d5b3a7ac8d154562) article by Craig Lazzeretti called "30 Greatest Surfers All Time".
- [Magicseaweed's](https://magicseaweed.com/news/msws-top-50-trending-surfers-of-2018/11117/) article called "MSW's Top 50 Trending Surfers of 2018".
