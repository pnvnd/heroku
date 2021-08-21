from flask import Flask, render_template, request

# Flask Web Application
app = Flask(__name__)

# Navigation
@app.route("/")
def index():
    return render_template("index.html")

# Run Flask Web Application
if __name__ == "__main__":
    app.run()