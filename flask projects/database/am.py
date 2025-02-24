from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


if __name__=='__main__':
    app.run(debug=True)