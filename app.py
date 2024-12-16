import datetime
import random

import flask

app = flask.Flask(__name__)
cars = ['Chevrolet', 'Renault', 'Ford', "Mercedes", 'BMW']
cats = ['Русская голубая', 'Корниш-рекс',
        'Шотландская вислоухая', 'Мейн-кун',
        'Манчкин']
count = 0

@app.route('/hello')
def hello():
    return '<h1>Начало новой жизни для всех.</h1>'


@app.route('/cars')
def cars_list():
    return f'<h2>Cars :{cars}</h2>'


@app.route('/cats')
def cats_list():
    choice = random.choice(cats)
    return f'<h2>Cat :{choice}</h2>'


@app.route('/time/now')
def time():
    cur_time = datetime.datetime.now().strftime('Time: %H:%M:%S')
    return f'<h2>Current time :{cur_time}</h2>'


@app.route('/time/future')
def time_future():
    cur_time = datetime.timedelta(hours=datetime.datetime.now().hour + 1, minutes=datetime.datetime.now().minute,
                                  seconds=datetime.datetime.now().second)
    return f'<h2>Future time :{cur_time}</h2>'


@app.route('/counter')
def count_sh():
    global count
    count += 1
    return f'<h2>Future time :{count}</h2>'


if __name__ == "__main__":
    app.run(debug=True)
