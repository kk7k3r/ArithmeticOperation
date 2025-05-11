from flask import Flask
from Web.controllers.main_controllers import controllers

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.register_blueprint(controllers)
    return app

if __name__ == "__main__":
    web_app = create_app()
    web_app.run(debug=True)