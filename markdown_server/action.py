from markdown_server import domain, responder


def index(path: str) -> tuple[str, int]:
    content = domain.generate_content(domain.load_file(path))
    return responder.response_content(content)
