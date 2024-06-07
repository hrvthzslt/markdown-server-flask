from flask import Blueprint

from src.blueprint.markdown_server import action
from src.infrastructure.cache import cache

blueprint = Blueprint("markdown_server_app", __name__, template_folder="templates")


@blueprint.route("/", defaults={"path": ""})
@blueprint.route("/<path:path>")
@cache.cached(timeout=60)
def index(path: str):
    return action.index(path)
