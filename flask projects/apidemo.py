from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/greet/<string:name>',methods=['GET'])
def greet(name):
    return jsonify(message=f'{name}!')

if __name__=='__main__':
    app.run(debug=True)