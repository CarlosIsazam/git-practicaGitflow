from distutils.debug import DEBUG
from pickle import TRUE
from src.app import app
HOST="localhost"
PORT=4000
DEBUG=TRUE


if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)