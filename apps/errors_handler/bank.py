import csv
import logging
from typing import Optional

import flask
from flask_wtf import FlaskForm
from werkzeug.exceptions import InternalServerError
from wtforms import IntegerField
from wtforms.validators import InputRequired

app = flask.Flask(__name__)
import logging.config

from apps.basicLog.loging_config import dict_donfig

logging.config.dictConfig(dict_donfig)

submoduleLogger = logging.getLogger("module_logger.submodule_logger")
submoduleLogger.setLevel("DEBUG")


class RegistrationForm(FlaskForm):
    a = IntegerField(default=10, validators=[InputRequired()])
    b = IntegerField(default=0, validators=[InputRequired()])


# logger = logging.getLogger("bank")


@app.route('/bank/<string:branch>/<int:person_id>/')
def code_sub(branch: str, person_id: int):
    branch_name = f"bank_data/{branch}.csv"
    with open(branch_name, 'r', encoding='utf-8') as fi:
        reader = csv.DictReader(fi, delimiter=',')

        for record in reader:
            if int(record['id']) == person_id:
                return f"Person Account: {record['name']} and name: {record['name']}"
        else:
            return 'Bad request', 404


# @app.errorhandler(InternalServerError)
# def handler_exception(e: InternalServerError):
#     import datetime
#     original_error: Optional[Exception] = getattr(e, "original_exception", None)
#     print(original_error)
#     if isinstance(original_error, FileNotFoundError):
#         with open('./error_log.log', 'a') as fe:
#             fe.write(f"Error occurred by {original_error} exception, time: {datetime.datetime.now()}\n")
#     return "Unexpected error.", 500


@app.errorhandler(Exception)
def handler_exception(e: InternalServerError):
    # logger.error("Some exception occurred.")
    original_error: Optional[Exception] = getattr(e, "original_exception", None)
    print(original_error)
    if isinstance(original_error, FileNotFoundError):
        submoduleLogger.error(f"Файл не найден, либо поврежден. Ошибка: {original_error.strerror}")
    elif isinstance(original_error, OSError):
        submoduleLogger.error(f"Нельзя получить нужную карточку. Ошибка: {original_error.strerror}")

    return "Internal server error", 500


if __name__ == "__main__":
    # formated = """{"time":"%(asctime)s", "log_level":"%(levelname)s", "msg":"%(message)s"},"""
    # logging.basicConfig(level=logging.DEBUG, filename="bank.json", format=formated, filemode='w', encoding='utf-8')
    submoduleLogger.info("Start server.")
    app.run(debug=True)
