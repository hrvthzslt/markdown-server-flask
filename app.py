from flask import Flask

from src.blueprint.markdown_server.blueprint import blueprint as markdown_server_blueprint
from src.infrastructure.cache import cache

app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(markdown_server_blueprint)


if __name__ == "__main__":
    app.run()
