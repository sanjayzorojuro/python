from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Running in VS Code.Hello sir i am cooking something."

if __name__ == '__main__':
    app.run(debug=True)