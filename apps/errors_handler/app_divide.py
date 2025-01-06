import logging

import flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired

app = flask.Flask(__name__)

logger = logging.getLogger("Divide")


class RegistrationForm(FlaskForm):
    a = IntegerField(default=10, validators=[InputRequired()])
    b = IntegerField(default=0, validators=[InputRequired()])


@app.route('/divide/', methods=["POST"])
def code_sub():
    form_data = RegistrationForm()
    if form_data.validate_on_submit():
        a, b = form_data.a.data, form_data.b.data,
        res = f"{a / b:.2f}"
        logger.debug(f"Form is valid. a={a}, b={b}")
        return f"a / b = {res}"
    # logger.error(f"Form is not valid, error={form_data.errors} ")
    return f"Bad request. Error = {form_data.errors}", 400


@app.errorhandler(ZeroDivisionError)
def handler_exception(e: ZeroDivisionError):
    logger.exception(f"Invalid division on zero. code: 400", exc_info=e)
    return "Invalid division on zero.", 400


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Beginning to work")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
