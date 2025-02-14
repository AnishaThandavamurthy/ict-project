from flask import Flask,render_template,redirect,request,url_for
app =Flask(__name__)

users = {"raj":"raj123"}
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        print('anisha...........................')
        username = request.form.get('username')
        password = request.form.get('password')
        if users[username]==password:
            return redirect(url_for('home'))
        else:
            return 'Invalid details please try again later!!!!!'

    
    return render_template('login.html')

@app.route('/movie', methods=['POST','GET'])
def movie():
    if request.method=='POST':
        return redirect(url_for('movie'))
    return render_template('movie.html')

@app.route('/puzzle', methods=['POST','GET'])
def puzzle():
    if request.method=='POST':
        return redirect(url_for('puzzle'))
    return render_template('puzzle.html')

@app.route('/cartoon', methods=['POST','GET'])
def cartoon():
    if request.method=='POST':
        return redirect(url_for('cartoon'))
    return render_template('cartoon.html')

@app.route('/health', methods=['POST','GET'])
def health():
    if request.method=='POST':
        return redirect(url_for('health'))
    return render_template('health.html')

@app.route('/exam', methods=['POST','GET'])
def exam():
    if request.method=='POST':
        return redirect(url_for('exam'))
    return render_template('exam.html')

@app.route('/woman', methods=['POST','GET'])
def woman():
    if request.method=='POST':
        return redirect(url_for('woman'))
    return render_template('woman.html')

@app.route('/sunday', methods=['POST','GET'])
def sunday():
    if request.method=='POST':
        return redirect(url_for('sunday'))
    return render_template('sunday.html')

@app.route('/epaper', methods=['POST','GET'])
def epaper():
    if request.method=='POST':
        return redirect(url_for('epaper'))
    return render_template('epaper.html')

@app.route('/religion', methods=['POST','GET'])
def reg():
    if request.method=='POST':
        return redirect(url_for('religion'))
    return render_template('religion.html')



if __name__=='__main__':
    app.run(debug=True)