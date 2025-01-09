import flask

app = flask.Flask(__name__)
host = "0.0.0.0"
port = 5000


@flask.route("/start_app/<name_user>")
def run_app(name_user: str):
    return flask.make_response(
        flask.jsonify(
            {"massage": f"Hello from {name_user}, from app."}
        ), 200
    )


if __name__ == "__main__":
    app.run(host=host, port=port)
