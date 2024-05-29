from flask import Flask

from markdown_server.app import app as markdown_server_app

app = Flask(__name__)
app.register_blueprint(markdown_server_app)


if __name__ == "__main__":
    app.run()
