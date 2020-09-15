from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from models import init_db
from view import blue

app = Flask(__name__)
app.register_blueprint(blueprint=blue)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

init_db(app)

if __name__ == '__main__':
    app.run(debug=True)