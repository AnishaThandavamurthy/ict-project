from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate

app = Flask(__name__)
app.debug=True

    
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

migrate=Migrate(app,db)



class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(20),unique=False,nullable=False)
    last_name=db.Column(db.String(20),unique=False,nullable=False)
    age=db.Column(db.Integer,nullable=False)

def __repr__(self):
        return f"Name:{self.first.first_name},Age:{self.age}"




@app.route('/home')
def home():
    return render_template('home.html')
 
@app.route('/')
def index():
    users=User.query.all()
    return render_template('index.html' ,users=users)

@app.route('/add_data')
def add_data():
    return render_template('adduser.html')

@app.route('/add',methods=["POST"])
def user():    
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    age=request.form.get("age")


    if first_name !=''and last_name !='' and age is not None:
        p= User(first_name=first_name,last_name=last_name,age=age)
        db.session.add(p)
        db.session.commit()
        return redirect('/') 
    else:
        return redirect('/')
    
    

@app.route('/delete/<int:id>')
def erase(id):
    data=User.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')



if __name__=='__main__':
    with app.app_context():
         db.create_all()
    app.run(debug=True)