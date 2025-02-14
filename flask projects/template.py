from flask import Flask

app = Flask(__name__)

@app.route('/')
def about():
    return "<html><body><h1>Welcome to vidys vikas</h1></body></html>"

if __name__ =='__main__':
    app.run(debug =True)
