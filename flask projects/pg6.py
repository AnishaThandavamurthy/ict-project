from flask import Flask

app = Flask(__name__)

@app.route('/')



def user(name):
    temp1 = f'<h1>hello,{name}</h1>'

    temp2 = '<p>MR ,{name}, check the name in the <strong>browser address bar </strong>and reload the page.</p>'
    return temp1+ temp2 

if __name__ =='__main__':
    app.run(debug =True)