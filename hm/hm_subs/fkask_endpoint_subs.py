import flask
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

from hm_subprocess import run_sub_code

app = flask.Flask(__name__)


class RegistrationForm(FlaskForm):
    code = StringField(validators=[InputRequired("Необходим ввод")])
    timeout = IntegerField(default=10)


@app.route('/code_sub', methods=["POST"])
def code_sub():
    form_data = RegistrationForm()
    if form_data.validate_on_submit():
        code, timeout = form_data.code.data, form_data.timeout.data
        stdout, stderr, killed = run_sub_code(code, timeout)
        return f"Stdout - {stdout}, stderr - {stderr}" + (f"Process was killed." if killed else "")
    return f"Invalid  input, {form_data.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
