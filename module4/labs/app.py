import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return """

    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Viettel Devnet</title>

    
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css"
        integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">
        </head>

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

    .cover-container {
    max-width: 60vw;
    }

    .nav-link {
        padding: 0.25rem 0;
        font-weight: 700;
        color: rgba(255,255,255,0.5);
        margin-left: 1rem;
        border-bottom: 0.25rem solid transparent;
    }

    .nav-link:hover{
        color: rgba(255,255,255,0.5);
        border-bottom-color:rgba(255,255,255,0.5);
    }

    .nav-link.active {
        color: white;
        border-bottom-color:white;

    }

    .btn-secondary, .btn-secondary:hover{
        color: #333;
        text-shadow: none;
    }

    h1 {
        margin-top: 100px;
        color: white;
        text-align: center;
        font-family: verdana;
        font-size: 300%;
    }

    div {
        margin-top: 100px;
        margin-left: 500px;
    }
    
    </style>

    <h1>Welcome to Devnet Course 2022</h1>
    <div>
        <a href="https://github.com/devnetciscovn/devnet_course" class="btn btn-lg btn-secondary font-weight-bold border-white bg-white">GitHub Repositories</a>
        <a href="https://hub.docker.com/repository/docker/devnetvn/simple-web-app" class="btn btn-lg btn-secondary font-weight-bold border-white bg-white">Docker Hub</a>
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