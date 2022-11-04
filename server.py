from flask import Flask, render_template

app = Flask(__name__)
@app.route('/play')
def levelOne():
    return render_template("index.html", n=3, color="blue")
@app.route('/play/<int:n>')
def levelTwo (n) :
    return render_template("index.html",n=n, color="blue")

@app.route('/play/<int:n>/‹string:color>')
def levelThree(n, color):
    return render_template ("index.html",n=n, color=color)
if __name__=="__main__":
    app.run(debug=True)