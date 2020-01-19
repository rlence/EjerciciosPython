from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo'

@app.route('/rick')
def hello_rick():
    return 'Hola Full Stack Enginer and Software Enginer Ricardo Lence'


if __name__ == '__main__':
    app.run()