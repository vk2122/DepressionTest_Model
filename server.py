from flask import Flask, request, render_template
from models import Model
#from facecv import run
import os

#run()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    if prediction[0] == 0:
        result1 = 'Your Test result : No Depression'
    if prediction[0] == 1:
        result1 = 'Your Test result : Mild Depression'
    if prediction[0] == 2:
        result1 = 'Your Test result : Moderate Depression'
    if prediction[0] == 3:
        result1 = 'Your Test result : Moderately severe Depression'
    if prediction[0] == 4:
        result1 = 'Your Test result : Severe Depression'
    return render_template("result.html", result=result1)


app.secret_key = os.urandom(12)
app.run(port=5987, host='0.0.0.0', debug=True)