import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from functions import search_tag


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_key = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = search_tag(search_key)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    if search_key:
        return render_template('post_list.html', tag=search_key, posts=posts)
    return 'Вы ввели ничего'

