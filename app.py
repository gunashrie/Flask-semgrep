from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f"<html>Hello, {name}!</html>"

if __name__ == '__main__':
    app.run(debug=True)
