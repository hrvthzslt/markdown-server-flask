from typing import Optional

from flask import render_template

from markdown_server import domain

type ActionResult = Optional[domain.Content]


def response_content(action_result: ActionResult) -> tuple[str, int]:
    if action_result is None:
        return render_template("404.html"), 404

    return (
        render_template(
            "index.html",
            content=action_result["content"],
            title=action_result["title"],
        ),
        200,
    )
