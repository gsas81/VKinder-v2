class BotResponsesUser:
    def __init__(self):
        self.main_menu = "Отправьте:\n " \
                         "1 - Начать поиск\n " \
                         "2 - Редактировать свои данные(Лучше указать подробнее, чтобы поиск был более точным)\n " \
                         "3 - Просмотреть избранный список\n " \
                         "4 - Просмотреть чёрный список\n " \
                         "5 - Очистить историю поиска\n " \
                         "0 - Завершить"

        self.list_editor = "Отправьте:\n " \
                           "1 - Далее\n " \
                           "2 - Удалить из списка\n " \
                           "0 - Завершить просмотр"

        self.full_data_editor = "Отправьте:\n " \
                                "0 - Завершить редактирование\n " \
                                "100 - Вывести имеющиеся данные\n " \
                                "-1 - Заменить имеющиеся данные, данными из профиля\n " \
                                "1 - Изменить приоритет поиска по полу\n " \
                                "2 - Изменить возраст\n " \
                                "3 - Изменить город\n " \
                                "4 - Изменить семейное положение\n " \
                                "5 - Изменить любимые телепередачи\n " \
                                "6 - Изменить любимые цитаты\n " \
                                "7 - Изменить Ваши интересы\n " \
                                "8 - Изменить любимые игры\n " \
                                "9 - Изменить любимые книги\n " \
                                "10 - Изменить информацию о себе\n " \
                                "11 - Изменить деятильность\n " \
                                "12 - Изменить любимую музыку\n " \
                                "13 - Изменить любимые фильмы\n " \
                                "14 - Изменить отношение к алкоголю\n " \
                                "15 - Изменить источник вдохновения\n " \
                                "16 - Изменить приоритет главного в жизний\n " \
                                "17 - Изменить приоритет главного в людях\n " \
                                "18 - Изменить приоритет политичиских взглядов\n " \
                                "19 - Изменить мировазрение\n " \
                                "20 - Изменить отношение к курению\n"

        self.marital_status = "1 — не женат/не замужем\n" \
                              "2 — есть друг/есть подруга\n" \
                              "3 — помолвлен/помолвлена\n" \
                              "4 — женат/замужем\n" \
                              "5 — всё сложно\n" \
                              "6 — в активном поиске\n" \
                              "7 — влюблён/влюблена\n" \
                              "8 — в гражданском браке\n"

        self.user_opinion = "Отправьте:\n" \
                            "1 - Если кандидат понравился\n" \
                            "2 - Добавить в чёрный список\n" \
                            "3 - далее\n" \
                            "0 - завершить поиск"

        self.gender_priority = "Введите приоритет поиска кандидатов по полу:\n" \
                               "0 - Любой пол\n" \
                               "1 - Женский пол\n" \
                               "2 - Мужской пол\n"

        self.attitude = "1 — резко негативное\n" \
                        "2 — негативное\n" \
                        "3 — компромиссное\n" \
                        "4 — нейтральное\n" \
                        "5 — положительное\n"

        self.main_life = "Изменить приоритет главного в жизний:\n " \
                         "1 — семья и дети\n" \
                         "2 — карьера и деньги\n" \
                         "3 — развлечения и отдых\n" \
                         "4 — наука и исследования\n" \
                         "5 — совершенствование мира\n" \
                         "6 — саморазвити\n" \
                         "7 — красота и искусство\n" \
                         "8 — слава и влияние\n"

        self.main_people = "Изменить приоритет главного в людях:\n" \
                           "1 — ум и креативность\n" \
                           "2 — доброта и честность\n" \
                           "3 — красота и здоровье\n" \
                           "4 — власть и богатство\n" \
                           "5 — смелость и упорство\n" \
                           "6 — юмор и жизнелюбие"

        self.political_view = "Изменение политичиский взгляд:\n" \
                              "1 — коммунистические\n" \
                              "2 — социалистические\n" \
                              "3 — умеренные\n" \
                              "4 — либеральные\n" \
                              "5 — консервативные\n" \
                              "6 — монархические\n" \
                              "7 — ультраконсервативны\n" \
                              "8 — индифферентные\n" \
                              "9 — либертарианские"