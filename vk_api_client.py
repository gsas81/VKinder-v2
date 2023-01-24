import requests
from functools import wraps
import time


class CodeError(Exception):
    """Выбрасывается если запрос вернул код response (400-599)"""
    pass


def _check_response(response_code):
    if 400 <= response_code <= 499:
        raise CodeError("сервер не смог обработать запрос")

    if 500 <= response_code <= 599:
        raise CodeError("сервер не смог ответить на запрос")


def connection_attempt_decor(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        for attempt in range(1, 4):
            result_vk_method = f(*args, **kwargs)
            if result_vk_method is not None:
                return result_vk_method
            time.sleep(3)
        return "Сервер не отвечает, попробуйте написать позже"

    return wrapped


class VkApiClient:
    def __init__(self, token_user_vk):
        self.url = 'https://api.vk.com/method/'
        self.params = {
                        'access_token': token_user_vk,
                        'v': 5.131
        }

    @connection_attempt_decor
    def vk_method(self, method, params):
        params = {**self.params, **params}
        result_search = requests.get(self.url + method, params=params)
        try:
            _check_response(result_search.status_code)
        except NameError:
            return
        except CodeError:
            return
        result_json = result_search.json()
        return result_json


def call_vk_method(method, params, user_active, vk_method_class, vk):
    response = vk_method_class.vk_method(method, params)
    if response == "Сервер не отвечает, попробуйте написать позже":
        user_active.write_msg(vk, f"Сервер не отвечает, попробуйте написать позже")
        return
    else:
        return response
