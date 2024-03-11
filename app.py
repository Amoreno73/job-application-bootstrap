from flask import Flask, render_template

app = Flask(__name__)
#creating new web application called app.

@app.route("/")
#decorator in python. it wraps the function to extend its behavior. 
# this tells flask that whenver a user visits the main page of the website, flask should call the function 
# directly below the decorator, which is index()

def index():
    return render_template("index.html")
# the render template function generates an html page for the user
# index html is the name of the template that the render template method will use for thte page. 

app.run(debug=True, port=5001)
# app starts running. #the app will tell us errors with debug = True.
# the port will communicate with outside world. -> local computer

