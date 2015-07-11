from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"


@app.route("/hello/<name>")
def hello_person(name):
    return render_template('name.html', name = name.title())
    
    
@app.route("/jedi/<firstname>/<lastname>")
def jedi (firstname, lastname):
    jedi_name = firstname[0:2] + lastname [0:3]
    print jedi_name;
    
    return render_template('jedi.html', firstname = firstname.title(),lastname = lastname.title(), jedi_name = jedi_name.title())
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))