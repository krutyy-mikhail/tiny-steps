import flask
from flask import render_template


app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Здесь будет главная'


@app.route('/all/')
def all_teachers():
    return 'Здесь будут преподаватели'


@app.route('/goals/<goal>/')
def goal(goal):
    return 'Здесь будет цель'


@app.route('/profiles/<int:teacher_id>/')
def profile(teacher_id):
    return 'Здесь будет профиль учителя'


@app.route('/request/')
def search():
    return 'Здесь будет заявка на подбор'


@app.route('/request_done/')
def request_done():
    return 'заявка на подбор отправлена'


@app.route('/booking/<int:teacher_id>/<day>/<time>/')
def booking(teacher_id, day, time):
    return f'здесь будет форма бронирования {teacher_id}'


@app.route('/booking_done/')
def booking_done(teacher_id, day, time):
    return 'заявка отправлена'


if __name__ == '__main__':
    app.run()
