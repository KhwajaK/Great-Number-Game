from flask import Flask, session, redirect, render_template, request
import random

app = Flask(__name__)
app.secret_key = "passweird"

@app.route("/")
def index():
    if "num" and "guess" not in session:
        session["num"] = random.randint(1, 100)
    return render_template("index.html")
    
@app.route("/guess", methods=["POST"])
def guess():
    session['guess'] = int(request.form['guess'])
    print(session["guess"])
    return redirect ('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(port=8000,debug=True)