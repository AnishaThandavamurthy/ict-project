from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def kp():
    return render_template('kp.html')


@app.route('/state')
def kp1():
    return render_template('state.html')

@app.route('/country')
def kp2():
    return render_template('country.html')

@app.route('/cricket')
def kp3():
    return render_template('cricket.html')

@app.route('/health')
def kp4():
    return render_template('health.html')

@app.route('/sports')
def kp5():
    return render_template('sports.html')

@app.route('/cinema')
def kp6():
    return render_template('cinema.html')

@app.route('/politics')
def kp7():
    return render_template('politics.html')

@app.route('/commerce')
def kp8():
    return render_template('commerce.html')

@app.route('/cook')
def kp9():
    return render_template('cook.html')

if __name__=='__main__':
    app.run(debug=True)
