from flask import Flask ,render_template
app=Flask(__name__)

@app.route('/')
def Hello():
    return render_template('index.html',name='Anisha')


@app.route('/tablepage')
def hello():
    return render_template('tablepage.html',name='Raksh',clg_name='VVIET',gen='Male',address='kuvempunagar,mysuru',state='Karnataka',age='25',place='mysuru')


@app.route('/form')
def form():
    return render_template('form.html',name='Anu')


if __name__ == '__main__':
    app.run(debug=True)
