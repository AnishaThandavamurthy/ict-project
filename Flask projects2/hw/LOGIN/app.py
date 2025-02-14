from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate


app=Flask(__name__)
app.debug=True

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///log.db'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class login(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(20),unique=False,nullable=False)
    password=db.Column(db.String(20),unique=True,nullable=False)

def __repr__(self):
    return f"Name:{self.user_name},password:{self.password}"

@app.route('/')
def index():
    users=login.query.all()

    return render_template('index.html',users=users)


@app.route('/adduser')
def adduser():
    return render_template('login.html')

@app.route('/add',methods=["POST"])
def user():
    user_name=request.form.get("user_name")
    password=request.form.get("password")

    if user_name !='' and password is not None:
        p=login(user_name=user_name,password=password)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    
    else:
        return redirect('/')
    
@app.route('/delete/<int:id>')
def erase(id):
    data=login.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)