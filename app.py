from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/results/<int:score>')
def results(score):
    return 'The Person is failed with average marks of '+str(score)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        sst = float(request.form['sst'])
        english = float(request.form['english'])
        hindi = float(request.form['hindi'])

        avg_marks = (maths+science+sst+english+hindi)/5

        if avg_marks>50:

            return render_template('result_.html',results=avg_marks)

        else:

            return redirect(url_for('results',score=avg_marks))

if __name__ == '__main__':
    app.run(debug=True)