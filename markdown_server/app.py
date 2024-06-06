from flask import Blueprint

from markdown_server import action
from infrastructure.cache import cache

app = Blueprint("markdown_server_app", __name__, template_folder="templates")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
@cache.cached(timeout=60)
def index(path: str):
    return action.index(path)
