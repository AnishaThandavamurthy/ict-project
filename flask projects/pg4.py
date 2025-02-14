from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    personal = f'<h1>hello,{name}</h1>'

    instruc = '<p>MR {name} check the name in the <strong>browser address bar </strong>and reload the page.</p>'
    return personal+ instruc 

if __name__ =='__main__':
    app.run(debug =True)
