from input import AppConfig
from storage import WorkingDatabase
from vk_api_client import VkApiClient, call_vk_method
from users import UserVkTinder
from bot_responses import BotResponsesUser
from main_menu import Menu
from search import SearchCandidate
import re
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def fetch_user_vk(user_id, user_active, db, vk):
    result = db.select_user_id(user_id)
    if result is None:
        get_user_data(user_active, user_id, vk)
        db.insert_data_user(user_active)
        user_active.write_msg(vk, f"Здравствуйте, {user_active.first_name}!")
    else:
        result = db.select_full_data(user_id)
        user_active.import_full_data(result)
        user_active.write_msg(vk, f"Здравствуйте, {user_active.first_name}!")


def get_user_data(user_active, user_id, vk):
    data = vk.method('users.get', {'user_id': user_id, 'fields': 'first_name, sex, tv, quotes, personal, '
                                                                 'interests, games, books, about, activities, '
                                                                 'music, movies, bdate, city, relation'})
    user_active.full_user_data(user_id, data)
    return


def fetch_user_token(user_active, vk_method_class, vk, config, db, long_poll):
    user_id = user_active.user_id
    token_user_vk = db.select_full_token(user_id)

    for step in range(0, 3):
        vk_method_class.params = {
            'access_token': token_user_vk,
            'v': 5.131
        }
        params = {
            'count': 40,
            'sort': 0,
        }
        method = 'users.search'
        test_token = call_vk_method(method, params, user_active, vk_method_class, vk)
        if 'error' not in test_token:
            return 'active token'
        else:
            user_active.write_msg(vk, f"Перейдите по ссылке и подтвердите доступ к нужной информации для поиска "
                                      f"кандидатов, после отправьте полученую ссылку боту:\n"
                                      f"{config.application_access_link}")
            for token_event in long_poll.listen():
                if token_event.type == VkEventType.MESSAGE_NEW and token_event.user_id == user_active.user_id:

                    if token_event.to_me:
                        request_token = token_event.text
                        pattern = re.compile(r'(\S+)token=(\w+)(\S+)')
                        token_user_vk = pattern.sub(r"\2", request_token)
                        db.update_token(user_id, token_user_vk)
                        break
    user_active.write_msg(vk, f"Сервис не отвечает, или не действителен токен")
    return 'inactive token'


def main():
    config = AppConfig()
    config.input_data()
    db = WorkingDatabase(config.dbname, config.user_bd, config.password)
    vk = vk_api.VkApi(token=config.token)
    bot_msg = BotResponsesUser()
    long_poll = VkLongPoll(vk)

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text
                print(request)
                user = UserVkTinder()
                fetch_user_vk(event.user_id, user, db, vk)
                request = request.lower()
                if request == "привет" or request == "хай":
                    token_user = '?'
                    vk_method_class = VkApiClient(token_user)
                    active_token = fetch_user_token(user, vk_method_class, vk, config, db, long_poll)
                    if active_token == 'inactive token':
                        continue

                    search = SearchCandidate(vk, user, db, bot_msg, long_poll, vk_method_class)
                    menu = Menu(user, vk, long_poll, db, bot_msg, get_user_data, search)
                    menu.main_menu(menu)
                else:
                    user.write_msg(vk, "Напишите 'Привет' или 'Хай' Чтобы мы могли приступить к поиску!")


if __name__ == '__main__':
    main()
