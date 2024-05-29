from markdown_server import domain, responders


def index(path: str) -> tuple[str, int]:
    content = domain.generate_content(domain.load_file(path))
    return responders.response_content(content)
