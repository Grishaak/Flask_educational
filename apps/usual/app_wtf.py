from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange, Optional
from validators.validator import length_check

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired("Необходим ввод"), Email("Неверная форма email")])
    phone = IntegerField(validators=[InputRequired(),
                                     NumberRange(min=10 ** 9, max=10 ** 10 - 1)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired(), length_check(max_len=10)])
    comment = StringField(validators=[Optional()])


@app.route("/registration", methods=["POST"])
def registration():
    form_data = RegistrationForm()
    if form_data.validate_on_submit():
        email, phone = form_data.email.data, form_data.phone.data
        return f"Successfully registered user {email} with phone +7{phone}"
    return f"Invalid  input, {form_data.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
