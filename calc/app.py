# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def math_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))

@app.route('/sub')
def math_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.route('/mult')
def math_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.route('/div')
def math_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def calc_operation(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(OPERATIONS[operation](a,b))
    
