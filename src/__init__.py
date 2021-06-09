from flask import Flask

app = Flask(__name__, template_folder='views')

app.secret_key = '3T6axyzGm2upcw5zvK3VpnuhZMTKh8QEgJBZKWSQg2p3Qp2N2wckQgBYx268RnJ3CLjuX8QcQkNYk9bMUyFKB9fc3Fjgy2KWgLWvLKMpKXKYD4ZwkBKQUyZ2v7L5McevkxKgjYYCWqk9MwRAFrqy'
#importando controles todo
from src.controllers import *


def create_app():
    app.run(debug=True) #arrancar la aplicacion