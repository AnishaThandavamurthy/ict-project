from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "hello,welcome to website with routing!!";

if __name__ == '__main__':
    app.run(debug =True)