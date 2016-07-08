from flask import Flask, request
app = Flask(__name__)

import application.models
import application.views

if __name__ == "__main__":
    app.run()
