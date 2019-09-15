from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings.settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from apps.tasks import bp

app.register_blueprint(bp, url_prefix='/tasks')


if __name__ == "__main__":
    app.run(debug=True)
