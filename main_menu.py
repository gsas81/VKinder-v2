from vk_api.longpoll import VkEventType


class Menu:
    def __init__(self, user_active, vk, long_poll, database, bot_msg, get_user_data, search):
        self.user_id = user_active.user_id
        self.user_active = user_active
        self.vk = vk
        self.long_poll = long_poll
        self.database = database
        self.bot_msg = bot_msg
        self.get_user_data = get_user_data
        self.search = search

    def user_update_sex(self):
        self.user_active.write_msg(self.vk, self.bot_msg.gender_priority)
        for sex_event in self.long_poll.listen():
            if sex_event.type == VkEventType.MESSAGE_NEW and sex_event.user_id == self.user_id:

                if sex_event.to_me:
                    update_sex_request = sex_event.text
                    try:
                        update_sex_request = int(update_sex_request)
                        if update_sex_request in range(0, 3):
                            self.database.update_sex(self.user_id, update_sex_request)
                            self.user_active.sex = update_sex_request
                            self.user_active.write_msg(self.vk, f"Приоритет изменён")
                            return
                    except ValueError:
                        pass
                    self.user_active.write_msg(self.vk, f"Не верное значение {update_sex_request}")
                    return

    def user_update_age(self):
        self.user_active.write_msg(self.vk, f"Введите сколько Вам полных лет")
        for age_event in self.long_poll.listen():
            if age_event.type == VkEventType.MESSAGE_NEW and age_event.user_id == self.user_id:

                if age_event.to_me:
                    update_age_request = age_event.text
                    try:
                        update_age_request = int(update_age_request)
                        self.database.update_age_user(self.user_id, update_age_request)
                        self.user_active.age = update_age_request
                        self.user_active.write_msg(self.vk, f"Возраст изменён на {update_age_request}")
                        return
                    except ValueError:
                        self.user_active.write_msg(self.vk, f"Не верное значение {update_age_request}")
                        return

    def user_update_city(self):
        self.user_active.write_msg(self.vk, f"Введите название Вашего города")
        for city_event in self.long_poll.listen():
            if city_event.type == VkEventType.MESSAGE_NEW and city_event.user_id == self.user_id:

                if city_event.to_me:
                    update_city_request = city_event.text
                    self.database.update_city(self.user_id, update_city_request)
                    self.user_active.city = update_city_request
                    self.user_active.write_msg(self.vk, f"Город изменён на {update_city_request}")
                    return

    def user_update_relation(self):
        self.user_active.write_msg(self.vk, f"Изменение семейного положения:\n{self.bot_msg.marital_status}")
        for relation_event in self.long_poll.listen():
            if relation_event.type == VkEventType.MESSAGE_NEW and relation_event.user_id == self.user_id:

                if relation_event.to_me:
                    update_relation = relation_event.text
                    try:
                        update_relation = int(update_relation)
                        if update_relation in range(1, 9):
                            self.database.update_relation(self.user_id, update_relation)
                            self.user_active.relation = update_relation
                            self.user_active.write_msg(self.vk, f"Приоритет изменён")
                            return
                    except ValueError:
                        pass
                    self.user_active.write_msg(self.vk, f"Не верное значение {update_relation}")
                    return

    def user_update_tv(self):
        self.user_active.write_msg(self.vk, f"Введите название ваших любимых передач")
        for tv_event in self.long_poll.listen():
            if tv_event.type == VkEventType.MESSAGE_NEW and tv_event.user_id == self.user_id:

                if tv_event.to_me:
                    update_tv_request = tv_event.text
                    self.database.update_tv(self.user_id, update_tv_request)
                    self.user_active.tv = update_tv_request
                    self.user_active.write_msg(self.vk, f"Список любимых передач изменён")
                    return

    def user_update_quotes(self):
        self.user_active.write_msg(self.vk, f"Введите название Ваших любимых цитат")
        for quotes_event in self.long_poll.listen():
            if quotes_event.type == VkEventType.MESSAGE_NEW and quotes_event.user_id == self.user_id:

                if quotes_event.to_me:
                    update_quotes_request = quotes_event.text
                    self.database.update_quotes(self.user_id, update_quotes_request)
                    self.user_active.quotes = update_quotes_request
                    self.user_active.write_msg(self.vk, f"Список любимых цитат изменён")
                    return

    def user_update_interests(self):
        self.user_active.write_msg(self.vk, f"Введите Ваши интересы")
        for interests_event in self.long_poll.listen():
            if interests_event.type == VkEventType.MESSAGE_NEW and interests_event.user_id == self.user_id:

                if interests_event.to_me:
                    update_interests_request = interests_event.text
                    self.database.update_interests(self.user_id, update_interests_request)
                    self.user_active.interests = update_interests_request
                    self.user_active.write_msg(self.vk, f"Список интересов изменён")
                    return

    def user_update_games(self):
        self.user_active.write_msg(self.vk, f"Введите название Ваших любимых игор")
        for games_event in self.long_poll.listen():
            if games_event.type == VkEventType.MESSAGE_NEW and games_event.user_id == self.user_id:

                if games_event.to_me:
                    update_games_request = games_event.text
                    self.database.update_games(self.user_id, update_games_request)
                    self.user_active.games = update_games_request
                    self.user_active.write_msg(self.vk, f"Список любимых игор изменён")
                    return

    def user_update_books(self):
        self.user_active.write_msg(self.vk, f"Введите название Ваших любимых книг")
        for books_event in self.long_poll.listen():
            if books_event.type == VkEventType.MESSAGE_NEW and books_event.user_id == self.user_id:

                if books_event.to_me:
                    update_books_request = books_event.text
                    self.database.update_books(self.user_id, update_books_request)
                    self.user_active.books = update_books_request
                    self.user_active.write_msg(self.vk, f"Список любимых книг изменён")
                    return

    def user_update_about(self):
        self.user_active.write_msg(self.vk, f"Введите информацию о себе")
        for about_event in self.long_poll.listen():
            if about_event.type == VkEventType.MESSAGE_NEW and about_event.user_id == self.user_id:

                if about_event.to_me:
                    update_about_request = about_event.text
                    self.database.update_about(self.user_id, update_about_request)
                    self.user_active.about = update_about_request
                    self.user_active.write_msg(self.vk, f"Информация изменена")
                    return

    def user_update_activities(self):
        self.user_active.write_msg(self.vk, f"Введите информацию о своей деятельности")
        for activities_event in self.long_poll.listen():
            if activities_event.type == VkEventType.MESSAGE_NEW and activities_event.user_id == self.user_id:

                if activities_event.to_me:
                    update_activities_request = activities_event.text
                    self.database.update_activities(self.user_id, update_activities_request)
                    self.user_active.activities = update_activities_request
                    self.user_active.write_msg(self.vk, f"Информация изменена")
                    return

    def user_update_music(self):
        self.user_active.write_msg(self.vk, f"Введите название Вашей любимой музыки")
        for music_event in self.long_poll.listen():
            if music_event.type == VkEventType.MESSAGE_NEW and music_event.user_id == self.user_id:

                if music_event.to_me:
                    update_music_request = music_event.text
                    self.database.update_music(self.user_id, update_music_request)
                    self.user_active.music = update_music_request
                    self.user_active.write_msg(self.vk, f"Список любимой музыки изменён")
                    return

    def user_update_movies(self):
        self.user_active.write_msg(self.vk, f"Введите название Вашей любимых фильмов")
        for movies_event in self.long_poll.listen():
            if movies_event.type == VkEventType.MESSAGE_NEW and movies_event.user_id == self.user_id:

                if movies_event.to_me:
                    update_movies_request = movies_event.text
                    self.database.update_movies(self.user_id, update_movies_request)
                    self.user_active.movies = update_movies_request
                    self.user_active.write_msg(self.vk, f"Список любимых фильмов изменён")
                    return

    def user_update_alcohol(self):
        self.user_active.write_msg(self.vk, self.bot_msg.attitude)
        for alcohol_event in self.long_poll.listen():
            if alcohol_event.type == VkEventType.MESSAGE_NEW and alcohol_event.user_id == self.user_id:

                if alcohol_event.to_me:
                    update_alcohol = alcohol_event.text
                    try:
                        update_alcohol = int(update_alcohol)
                        if update_alcohol in range(1, 6):
                            self.database.update_alcohol(self.user_id, update_alcohol)
                            self.user_active.alcohol = update_alcohol
                            self.user_active.write_msg(self.vk, f"Приоритет изменён")
                            return
                    except ValueError:
                        pass
                    self.user_active.write_msg(self.vk, f"Не верное значение {update_alcohol}")
                    return

    def user_update_inspired_by(self):
        self.user_active.write_msg(self.vk, f"Введите Ваш источник вдохнавения")
        for inspired_by_event in self.long_poll.listen():
            if inspired_by_event.type == VkEventType.MESSAGE_NEW and inspired_by_event.user_id == self.user_id:

                if inspired_by_event.to_me:
                    update_inspired_by = inspired_by_event.text
                    self.database.update_inspired_by(self.user_id, update_inspired_by)
                    self.user_active.inspired_by = update_inspired_by
                    self.user_active.write_msg(self.vk, f"Источник вдохнавния изменён")
                    return

    def user_update_life_main(self):
        self.user_active.write_msg(self.vk, self.bot_msg.main_life)
        for life_main_event in self.long_poll.listen():
            if life_main_event.type == VkEventType.MESSAGE_NEW and life_main_event.user_id == self.user_id:

                if life_main_event.to_me:
                    update_life_main = life_main_event.text
                    try:
                        update_life_main = int(update_life_main)
                        if update_life_main in range(1, 9):
                            self.database.update_life_main(self.user_id, update_life_main)
                            self.user_active.life_main = update_life_main
                            self.user_active.write_msg(self.vk, f"Приоритет изменён")
                            return
                    except ValueError:
                        pass
                    self.user_active.write_msg(self.vk, f"Не верное значение {update_life_main}")
                    return

    def user_update_people_main(self):
        self.user_active.write_msg(self.vk, self.bot_msg.main_people)
        for people_main_event in self.long_poll.listen():
            if people_main_event.type == VkEventType.MESSAGE_NEW and people_main_event.user_id == self.user_id:

                if people_main_event.to_me:
                    update_people_main = people_main_event.text
                    try:
                        update_people_main = int(update_people_main)
                        if update_people_main in range(1, 7):
                            self.database.update_people_main(self.user_id, update_people_main)
                            self.user_active.people_main = update_people_main
                            self.user_active.write_msg(self.vk, f"Приоритет изменён")
                            return
                    except ValueError:
                        pass
                    self.user_active.write_msg(self.vk, f"Не верное значение {update_people_main}")
                    return

    def user_update_political(self):
        self.user_active.write_msg(self.vk, self.bot_msg.political_view)
        for political_event in self.long_poll.listen():
            if political_event.type == VkEventType.MESSAGE_NEW and political_event.user_id == self.user_id:

                if political_event.to_me:
                    update_political = political_event.text
                    try:
                        update_political = int(update_political)
                        if update_political in range(1, 10):
                            self.database.update_political(self.user_id, update_political)
                            self.user_active.political = update_political
                            self.user_active.write_msg(self.vk, f"Приоритет изменён")
                            return
                    except ValueError:
                        pass
                    self.user_active.write_msg(self.vk, f"Не верное значение {update_political}")
                    return

    def user_update_religion(self):
        self.user_active.write_msg(self.vk, f"Введите Ваше мировозрение")
        for religion_event in self.long_poll.listen():
            if religion_event.type == VkEventType.MESSAGE_NEW and religion_event.user_id == self.user_id:

                if religion_event.to_me:
                    update_religion = religion_event.text
                    self.database.update_religion(self.user_id, update_religion)
                    self.user_active.religion = update_religion
                    self.user_active.write_msg(self.vk, f"Мировозрение изменено")
                    return

    def user_update_smoking(self):
        self.user_active.write_msg(self.vk, self.bot_msg.attitude)
        for smoking_event in self.long_poll.listen():
            if smoking_event.type == VkEventType.MESSAGE_NEW and smoking_event.user_id == self.user_id:

                if smoking_event.to_me:
                    update_smoking = smoking_event.text
                    try:
                        update_smoking = int(update_smoking)
                        if update_smoking in range(1, 6):
                            self.database.update_smoking(self.user_id, update_smoking)
                            self.user_active.smoking = update_smoking
                            self.user_active.write_msg(self.vk, f"Приоритет изменён")
                            return
                    except ValueError:
                        pass
                    self.user_active.write_msg(self.vk, f"Не верное значение {update_smoking}")
                    return

    def output_data(self):
        result = self.database.select_full_data(self.user_id)
        self.user_active.write_msg(self.vk, f"id: {result['id_user']}\n\nИмя: {result['first_name']}\n\n"
                                            f"Приоритет поиска по полу: {result['sex']}\n\nВозраст: "
                                            f"{result['age_user']}\n\nГород: {result['city']}\n\nСемейное положение: "
                                            f"{result['relation']}\n\nЛюбимые телепередачи: {result['tv']}\n\n"
                                            f"Любимые цитаты: {result['quotes']}\n\nИнтересы: {result['interests']}\n\n"
                                            f"Любимые игры: {result['games']}\n\nЛюбимые книги: {result['books']}\n\n"
                                            f"О себе: {result['about']}\n\n Деятильность: {result['activities']}\n\n"
                                            f"Любимая музыка: {result['music']}\n\nЛюбимые фильмы: {result['movies']}"
                                            f"\n\nОтношеник к алкоголю: {result['alcohol']}\n\nИсточник вдохновения: "
                                            f"{result['inspired_by']}\n\n Главное в жизни: {result['life_main']}\n\n"
                                            f"Главное в людях: {result['people_main']}\n\nПолитичиские взгляды: "
                                            f"{result['political']}\n\nМировозрение: {result['religion']}\n\n"
                                            f"Отношение к курению: {result['smoking']}")

    def user_update_full_data(self):
        self.get_user_data(self.user_active, self.user_id, self.vk)
        self.database.update_data_user(self.user_active)

    def user_data_editor(self, menu):
        self.user_active.write_msg(self.vk, self.bot_msg.full_data_editor)

        for data_editor_event in self.long_poll.listen():
            if data_editor_event.type == VkEventType.MESSAGE_NEW and data_editor_event.user_id == self.user_id:

                if data_editor_event.to_me:
                    menu_request = data_editor_event.text

                    if menu_request == "0":
                        return
                    if menu_request == "100":
                        menu.output_data()
                    if menu_request == "-1":
                        menu.user_update_full_data()
                    if menu_request == "1":
                        menu.user_update_sex()
                    if menu_request == "2":
                        menu.user_update_age()
                    if menu_request == "3":
                        menu.user_update_city()
                    if menu_request == "4":
                        menu.user_update_relation()
                    if menu_request == "5":
                        menu.user_update_tv()
                    if menu_request == "6":
                        menu.user_update_quotes()
                    if menu_request == "7":
                        menu.user_update_interests()
                    if menu_request == "8":
                        menu.user_update_games()
                    if menu_request == "9":
                        menu.user_update_books()
                    if menu_request == "10":
                        menu.user_update_about()
                    if menu_request == "11":
                        menu.user_update_activities()
                    if menu_request == "12":
                        menu.user_update_music()
                    if menu_request == "13":
                        menu.user_update_movies()
                    if menu_request == "14":
                        menu.user_update_alcohol()
                    if menu_request == "15":
                        menu.user_update_inspired_by()
                    if menu_request == "16":
                        menu.user_update_life_main()
                    if menu_request == "17":
                        menu.user_update_people_main()
                    if menu_request == "18":
                        menu.user_update_political()
                    if menu_request == "19":
                        menu.user_update_religion()
                    if menu_request == "20":
                        menu.user_update_smoking()
                    self.user_active.write_msg(self.vk, self.bot_msg.full_data_editor)

    def view_whitelist(self):
        result = self.database.select_full_whitelist(self.user_id)
        if result is None:
            self.user_active.write_msg(self.vk, 'В избранном нет кандидатов')
        while result is not None:
            age, first_name = self.search.candidate_data(result[0])
            self.search.photo_candidate(result[0], first_name, age, self.user_id, 'whitelist', self.search)
            self.user_active.write_msg(self.vk, self.bot_msg.list_editor)
            for whitelist_event in self.long_poll.listen():
                if whitelist_event.type == VkEventType.MESSAGE_NEW and whitelist_event.user_id == self.user_id:

                    if whitelist_event.to_me:
                        request_whitelist = whitelist_event.text
                        if request_whitelist == "1":
                            result = self.database.operations_fetchone()
                            break
                        elif request_whitelist == "2":
                            self.database.delete_whitelist(self.user_id, result[0])
                            self.user_active.write_msg(self.vk, 'Кандидат удалён из избранного')
                            self.database.select_full_whitelist(self.user_id)
                            result = self.database.operations_fetchone()
                            break
                        elif request_whitelist == "0":
                            return
                        else:
                            self.user_active.write_msg(self.vk, self.bot_msg.list_editor)

    def view_blacklist(self):
        result = self.database.select_full_blacklist(self.user_id)
        if result is None:
            self.user_active.write_msg(self.vk, 'Чёрный список пуст')
        while result is not None:
            age, first_name = self.search.candidate_data(result[0])
            self.search.photo_candidate(result[0], first_name, age, self.user_id, 'whitelist', self.search)
            self.user_active.write_msg(self.vk, self.bot_msg.list_editor)
            for blacklist_event in self.long_poll.listen():
                if blacklist_event.type == VkEventType.MESSAGE_NEW and blacklist_event.user_id == self.user_id:

                    if blacklist_event.to_me:
                        request_blacklist = blacklist_event.text
                        if request_blacklist == "1":
                            result = self.database.operations_fetchone()
                            break
                        elif request_blacklist == "2":
                            self.database.delete_blacklist(self.user_id, result[0])
                            self.user_active.write_msg(self.vk, 'Кандидат удалён из чёрного списка')
                            self.database.select_full_blacklist(self.user_id)
                            result = self.database.operations_fetchone()
                            break
                        elif request_blacklist == "0":
                            return
                        else:
                            self.user_active.write_msg(self.vk, self.bot_msg.list_editor)

    def main_menu(self, menu):
        self.user_active.write_msg(self.vk, self.bot_msg.main_menu)

        for menu_event in self.long_poll.listen():
            if menu_event.type == VkEventType.MESSAGE_NEW and menu_event.user_id == self.user_id:

                if menu_event.to_me:
                    menu_request = menu_event.text

                    if menu_request == "1":
                        self.search.candidate_search(self.search)
                    if menu_request == "2":
                        menu.user_data_editor(menu)
                    if menu_request == "3":
                        menu.view_whitelist()
                    if menu_request == "4":
                        menu.view_blacklist()
                    if menu_request == "5":
                        self.database.delete_search_history(self.user_id)
                        self.user_active.write_msg(self.vk, f"История поиска теперь пуста")
                    if menu_request == "0":
                        self.user_active.write_msg(self.vk, 'Сеанс завершён')
                        return
                    else:
                        self.user_active.write_msg(self.vk, self.bot_msg.main_menu)
