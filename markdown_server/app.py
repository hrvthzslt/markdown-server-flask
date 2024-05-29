from flask import Blueprint

from markdown_server import actions

app = Blueprint("markdown_server_app", __name__, template_folder="templates")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path: str):
    return actions.index(path)
