from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Under construction, at the order of Baevid Trapezius Guo."

if __name__ == '__main__':
    app.run()
