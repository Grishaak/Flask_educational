import datetime
import random

import flask

app = flask.Flask(__name__)
cars = ['Chevrolet', 'Renault', 'Ford', "Mercedes", 'BMW']
cats = ['Русская голубая', 'Корниш-рекс',
        'Шотландская вислоухая', 'Мейн-кун',
        'Манчкин']
count = 0


@app.route('/hello/<string:username>')
def hello(username):
    return f'Привет тебе дорогой {username}'


@app.route('/even/<int:number>')
def even_odd(number: any):
    if isinstance(number, int):
        return f'Это число {"не четное" if number % 2 else "четное"}'
    return f'Это не число ты ввел, друг.'


@app.route('/compare/<int:number>/<int:number_2>')
def compare(number: int, number_2: int):
    if number > number_2:
        res = '>'
    if number < number_2:
        res = '<'
    else:
        res = '=='
    return f"Результат: {number} {res} {number_2}"


@app.route('/hello-world/<string:name>')
def hello_world(name: str):
    from datetime import datetime
    weekday = datetime.now().strftime("%A")
    return f"Hello, {name}, today is {weekday}"


@app.route('/max-number/<path:numbers>')
def max_number(numbers: str):
    maximum = max(list(map(lambda x: int(x), numbers.split('/'))))
    return f"Максимальное из всех чисел: <b>{maximum}</b>"


if __name__ == "__main__":
    app.run(debug=True)
