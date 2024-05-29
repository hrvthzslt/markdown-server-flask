import io
from typing import Optional, TypedDict

import frontmatter
import markdown


class Content(TypedDict):
    title: str
    content: str


type LoadedFile = Optional[io]


def generate_content(file: LoadedFile) -> Content:
    if file is None:
        return None

    frontmatter_file = frontmatter.load(file)
    content = markdown.markdown(frontmatter_file.content, extensions=["fenced_code"])
    title = frontmatter_file.metadata.get("title", "Markdown Server")

    return {"title": title, "content": content}


def load_file(path: str) -> LoadedFile:
    try:
        return open("content/" + path + "/index.md", "r")
    except FileNotFoundError:
        return None
