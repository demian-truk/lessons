"""
# 1:
Создать Flask приложение, которое обрабатывает GET/POST запросы и выводит сообщение в консоль при помощи логгера.
Запустить приложение.

# 2:
Создать в Postman'е новый GET запрос и запустить его, проверить что Flask приложение выводит в консоль сообщения.

# 3:
Добавить в GET запрос параметры и вывести построчно их в консоль в формате "key: value".

# 4:
Создать в Postman'е новый POST запрос и вывести в консоль приложения параметры аналогично предыдущему заданию.
"""

import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


def dict_to_str(data: dict) -> str:
    result = []
    for key, value in data.items():
        result.append(f"{key}: {value}")
    return ", ".join(result)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info(dict_to_str(request.form.to_dict()))
        return request.form.to_dict()
    logger.info(dict_to_str(request.args.to_dict()))
    return request.args.to_dict()


if __name__ == "__main__":
    app.run()
