from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stureg.db'

db = SQLAlchemy(app)
migrate=Migrate(app,db)
#==============================================================================================================================

class Student(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(20),unique=False, nullable=False)
    last_name=db.Column(db.String(20),unique=False,nullable=False)
    dob=db.Column(db.String(20),unique=False,nullable=False)
    gender=db.Column(db.String(20),unique=False,nullable=False)
    email=db.Column(db.String(20),unique=False,nullable=False)
    phone=db.Column(db.String(20),unique=False,nullable=False)
    address=db.Column(db.String(20),unique=False,nullable=False)
    course=db.Column(db.String(20),unique=False,nullable=False)
    yos=db.Column(db.String(20),unique=False,nullable=False)

    def __repr__(self):
        return f"student({self.first_name},{self.last_name},{self.dob},{self.gender},{self.email},{self.phone},{self.address},{self.course},{self.yos})"
    
@app.route('/')
def index():
    students=Student.query.all()
    return render_template('student_index.html',students=students,name="Hemanth")
#==============================================================================================================================

@app.route('/addstudent')
def add():
    return render_template('studentreg.html')

@app.route('/add', methods=['POST'])
def user():
    id=request.form.get("id")
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    dob=request.form.get("dob")
    gender=request.form.get("gender")
    email=request.form.get("email")
    phone=request.form.get("phone")
    address=request.form.get("address")
    course=request.form.get("course")
    yos=request.form.get("yos")
    if first_name!='' and last_name!='' and dob!='' and gender!='' and email!='' and phone!='' and address!='' and course!='' and yos!='':
        p=Student(id=id,first_name=first_name,last_name=last_name,dob=dob,gender=gender,email=email,phone=phone,address=address,course=course,yos=yos)            
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('add'))
    
@app.route('/delete/<int:id>')
def delete(id):
    data=Student.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('index'))

if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
