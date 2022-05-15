import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return """
    <style>
    body {
        height: 100vh;
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
        url("https://www.indeawards.com/wp-content/uploads/2021/05/1617269319480-viettel_hq_10.jpg");
        background-size: cover;
        background-position: center;
        text-shadow: 0 0.05rem 0.1rem rgba(0, 0, 0, 0.5);
        box-shadow: inset 0 0 5rem rgba(0, 0, 0, 0.5);
    }

    h1 {
        margin-top: 100px;
        color: white;
        text-align: center;
        font-family: verdana;
        font-size: 300%;
    }
    </style>
    <div>
        <h1>Welcome to Devnet Course 2022</h1>
    </div>
    """

@app.route('/links')
def links():
    return """
    <br>
    <a href="https://github.com/devnetciscovn/devnet_course.git">Github repository</a>
    <br>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)