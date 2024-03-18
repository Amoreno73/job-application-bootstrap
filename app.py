from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # creating new web application called app.



app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLACHEMY_DATABASE_URI"] = "sqlite:///data2.db"

db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))
# this is creating the databases using sql alchemy


@app.route("/",methods=["GET","POST"]) 
# In web language, "GET" means someone is asking to see a page, like asking for a letter from the mailbox.
#  "POST" means someone is sending information to the page, like sending a letter back.

# Decorator in python. it wraps the function to extend its behavior. 
# this tells flask that whenver a user visits the main page of the website, flask should call the function 
# directly below the decorator, which is index()

def index():
    if request.method == "POST":
        #POST request, an arbitrary amount of data of any type can be sent to the server
        # in the body of the request message.
        first_name = request.form["first_name"]
        #when someone visits your website and sends info that is a post request.
        #if someone sent us info we see what it is
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"] 
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name, email=email, date=date_obj, occupation=occupation)

        db.session.add(form)
        db.session.commit()
        

    return render_template("index.html")
# the render template function generates an html page for the user
# index html is the name of the template that the render template method will use for thte page. 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)

app.run(debug=True, port=5001)
# app starts running. #the app will tell us errors with debug = True.
# the port will communicate with outside world. -> local computer

