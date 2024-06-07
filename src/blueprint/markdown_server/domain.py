import io
from typing import Optional, TypedDict

import frontmatter
import markdown


class Content(TypedDict):
    title: str
    content: str


def generate_content(file: Optional[io.TextIOWrapper]) -> Optional[Content]:
    if file is None:
        return None

    frontmatter_file = frontmatter.load(file)
    content = markdown.markdown(
        frontmatter_file.content, extensions=["fenced_code", "tables"]
    )
    title = frontmatter_file.metadata.get("title", "Markdown Server")

    return {"title": str(title), "content": content}


def load_file(path: str) -> Optional[io.TextIOWrapper]:
    try:
        return open("content/" + path + "/index.md", "r")
    except FileNotFoundError:
        return None
