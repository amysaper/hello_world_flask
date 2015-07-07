from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"


@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/jedi/<firstname>/<lastname>")
def jedi (firstname, lastname):
    jedi_name = firstname[0:2] + lastname [0:3]
    print jedi_name;
    html = """
        <h1>
            Hello {firstname} {lastname}!
        </h1>
        <h2>
            Your jedi name is {jedi_name}!
        </h2>
        <p>
            Here's one of the original jedis!
        </p>
        <img src="http://img2.wikia.nocookie.net/__cb20061223050619/starwars/images/6/61/AnakinSkywalker.jpg">
    """
    return html.format(jedi_name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))