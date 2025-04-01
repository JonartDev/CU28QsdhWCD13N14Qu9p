from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    html = render_template("index.html")
    with open("static/index.html", "w", encoding="utf-8") as file:
        file.write(html)
    return html

@app.route("/about")
def about():
    html = render_template("layouts/about.html")  # Adjusted to your directory structure
    with open("static/about.html", "w", encoding="utf-8") as file:
        file.write(html)
    return html

@app.route("/education")
def education():
    html = render_template("layouts/education.html")
    with open("static/education.html", "w", encoding="utf-8") as file:
        file.write(html)
    return html
@app.route("/skills")
def skills():
    html = render_template("layouts/skills.html")
    with open("static/skills.html", "w", encoding="utf-8") as file:
        file.write(html)
    return html

@app.route("/work")
def work():
    html = render_template("layouts/work.html")
    with open("static/work.html", "w", encoding="utf-8") as file:
        file.write(html)
    return html

if __name__ == "__main__":
    app.run(debug=True)
