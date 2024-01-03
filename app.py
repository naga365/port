
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/indexdata',methods=['post'])
def indexdata():
    Name=request.form['Name']
    # password=request.form['password']
    Email=request.form['Email']
    Subject=request.form['Subject']
    Message=request.form['Message']

    print(Name,Email,Subject,Message)

    return render_template('index.html',res="sent successfully")


if __name__=="__main__":
    app.run(debug=False,port=7001)
