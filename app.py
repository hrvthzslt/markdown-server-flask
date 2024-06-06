from flask import Flask

from markdown_server.app import app as markdown_server_app
from infrastructure.cache import cache

app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(markdown_server_app)


if __name__ == "__main__":
    app.run()
