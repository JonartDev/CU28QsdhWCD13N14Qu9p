from flask import Flask, render_template
import os

app = Flask(__name__)

# Ensure the "output" folder exists
if not os.path.exists("output"):
    os.makedirs("output")

@app.route("/")
def index():
    html_content = render_template("index.html")
    with open("output/index.html", "w") as f:
        f.write(html_content)
    return "Index page saved."

@app.route("/about")
def about():
    html_content = render_template("layouts/about.html")
    with open("output/about.html", "w") as f:
        f.write(html_content)
    return "About page saved."

@app.route("/education")
def education():
    html_content = render_template("layouts/education.html")
    with open("output/education.html", "w") as f:
        f.write(html_content)
    return "Education page saved."

@app.route("/work")
def work():
    html_content = render_template("layouts/work.html")
    with open("output/work.html", "w") as f:
        f.write(html_content)
    return "Work page saved."

if __name__ == "__main__":
    app.run(debug=True)
