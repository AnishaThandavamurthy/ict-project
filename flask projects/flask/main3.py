from flask import Flask ,render_template
app=Flask(__name__)


@app.route('/loop')
def hello():
    details=[
        {'name':'Anisha',"age":21,'gender':'female'},
        {'name':'megha',"age":25,'gender':'female'},
        {'name':'misha',"age":30,'gender':'female'},
        {'name':'misha',"age":30,'gender':'female'},
        {'name':'suresh',"age":35,'gender':'male'},
        {'name':'Guna',"age":28,'gender':'female'},
        {'name':'Shakthi',"age":32,'gender':'female'},
        {'name':'Kavan',"age":40,'gender':'male'},
        {'name':'anuj',"age":25,'gender':'male'},
        {'name':'mallesh',"age":30,'gender':'male'},
        {'name':'sara',"age":22,'gender':'female'},
    ]
    return render_template('looptable.html',data=details)


if __name__ == '__main__':
    app.run(debug=True)