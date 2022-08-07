import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from loader.utils import save_picture
from functions import append_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def get_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post():
    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        return 'Нет картинки или текста'

    if picture.filename.split('.')[-1] not in ['jpg', 'png']:
        logging.info('Загруженный файл не картинка')
        return 'Неверное расширение файла'

    try:
        picture_path = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    post = append_post({'pic': picture_path, 'content': content})

    return render_template("post_uploaded.html", post=post)



