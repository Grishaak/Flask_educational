import json
from urllib.parse import unquote_plus

import flask
from flask import request
app = flask.Flask(__name__)


@app.route("/summa/",
           methods=['GET'])
def search():
    numbers = request.args.getlist("number", type=int)
    if not numbers:
        return f"You must specify at last one number.", 400
    return f"Summa for {numbers} numbers is {sum(numbers)}."


@app.route("/combinations_get/",
           methods=['GET'])
def combinations_get():
    import itertools
    array_nums_1 = request.args.getlist("arr_1", type=int)
    array_nums_2 = request.args.getlist("arr_2", type=int)
    if (not array_nums_1) and (not array_nums_2):
        return f"You must specify at last one array of numbers.", 400
    return (
        f"All possible combinations for numbers_1 is {[i for i in itertools.permutations(array_nums_1,
                                                                                         len(array_nums_1))]}"
        f"\nAll possible combinations for numbers_1 is {array_nums_2}"
    )


@app.route("/summ_post_1/",
           methods=['POST'])
def combinations_post_1():
    array_nums_1 = request.form.getlist("arr_1", type=int)
    array_nums_2 = request.form.getlist("arr_2", type=int)
    result = ','.join([str(i + j) for i, j in zip(array_nums_1, array_nums_2)])
    return f"Result for summing two arrays is [{result}]"


@app.route("/summ_post_2/",
           methods=['POST'])
def combinations_post_2():
    form_data = request.get_data(as_text=True)
    decrypted = unquote_plus(form_data, encoding='utf-8')
    print(decrypted)
    return f"Result for summing two arrays is [{decrypted}]"


@app.route("/summ_post_3/",
           methods=['POST'])
def combinations_post_3():
    form_data = request.get_data(as_text=True)

    data = json.loads(form_data)
    print(data)
    result = ",".join(str(i + j) for i, j in zip(data['arr_1'], data['arr_2']))
    return f"Result for summing two arrays is [{result}]"


@app.route("/rotate/",
           methods=['POST'])
def rotate():
    # from collections import deque
    form_data = request.get_data(as_text=True)

    data = json.loads(form_data)
    data_list: list = data['array']
    minimum_index = data_list.index(min(data_list))
    return f"Result for rotated array is [{data}], rotated on {minimum_index}"


if __name__ == "__main__":
    app.run(debug=True)
