from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("layouts/about.html")

@app.route("/education")
def education():
    return render_template("layouts/education.html")

@app.route("/skills")
def skills():
    return render_template("layouts/skills.html")

@app.route("/work")
def work():
    return render_template("layouts/work.html")
    
@app.route("/contact")
def contact():
    return render_template("layouts/contact.html")

if __name__ == "__main__":
    app.run(debug=True)
