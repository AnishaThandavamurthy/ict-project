from flask import Flask ,render_template
app=Flask(__name__)

@app.route('/table')
def Hello():
    details=[
        {'name':'Anisha',"age":21,'gender':'female'},
        {'name':'megha',"age":25,'gender':'female'},
        {'name':'misha',"age":30,'gender':'female'},
    ]
        
        
    return render_template('table.html',data=details)


if __name__ == '__main__':
    app.run(debug=True)


        
        
    

