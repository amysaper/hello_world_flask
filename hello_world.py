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
            Hello {} {}!
        </h1>
        <h2>
            Your jedi name is {}!
        </h2>
        <p>
            Here's one of the original jedis!
        </p>
        <img src="http://img2.wikia.nocookie.net/__cb20061223050619/starwars/images/6/61/AnakinSkywalker.jpg">
    """
    return html.format(firstname.title(), lastname.title(), jedi_name.title())
    #firstname = firstname.title() etc for each variable, "named parameters" to convert to Jinja 

    
if __name__ == "__main__":
    print(jedi('amy', 'saper'))
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            