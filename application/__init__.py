from flask import Flask, request
from application.users.views import users

app = Flask(__name__)

app.register_blueprint(users, url_prefix='/users')

import application.models
import application.views

if __name__ == "__main__":
    app.run()
