from flask import Flask, render_template
app = Flask(__name__)

@app.route('/amazon')
def amazon():
    details=[
        {"img1":"https://images-eu.ssl-images-amazon.com/images/G/31/img23/PB/March/Bikram/QC_186_ALL_Customer_July_2._SY116_CB567469124_.jpg"},
        {"img2":"https://m.media-amazon.com/images/I/91OZ79o2bML._SX679_.jpg"},
        {"img3":"https://m.media-amazon.com/images/I/81NHlSFM8OL._AC_UL480_FMwebp_QL65_.jpg"},
        {"img4":"https://m.media-amazon.com/images/I/715UHrJkFHL._SX569_.jpg"}
    ]
    return render_template('amazon.html',data=details)

if __name__ == '__main__':
    app.run(debug=True)
