from flask import Flask, render_template, request

# Flask Web Application
app = Flask("main")

# Navigation
@app.route("/")
def index():
    return render_template("index.html")

# Run Flask Web Application
app.run()