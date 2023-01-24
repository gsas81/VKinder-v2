import random
import datetime
from operator import itemgetter
from vk_api_client import call_vk_method
from vk_api.longpoll import VkEventType


class SearchCandidate:
    def __init__(self, vk, user, database, bot_msg, long_poll, vk_method_class):
        self.vk = vk
        self.user_active = user
        self.database = database
        self.bot_msg = bot_msg
        self.long_poll = long_poll
        self.vk_method_class = vk_method_class

    def candidate_data(self, candidate_id):
        data = self.vk.method('users.get', {'user_id': candidate_id, 'fields': 'first_name, bdate'})
        first_name = data[0]['first_name']
        if 'bdate' in data[0]:
            age = data[0]['bdate'].split('.')
            number_of_elements = len(age)
            if number_of_elements == 3:
                now_date = datetime.datetime.now()
                birth_data = datetime.datetime(int(age[2]), int(age[1]), int(age[0]))
                age = (now_date - birth_data)
                age = str(age.days / 365)
            else:
                age = 'Возраст не указан'
        else:
            age = 'Возраст не указан'

        return age, first_name

    def evaluation_candidate(self, receiving):
        score = 0
        tv = self.user_active.tv.split(' ')
        quotes = self.user_active.quotes.split(' ')
        interests = self.user_active.interests.split(' ')
        games = self.user_active.games.split(' ')
        books = self.user_active.books.split(' ')
        about = self.user_active.about.split(' ')
        activities = self.user_active.activities.split(' ')
        music = self.user_active.music.split(' ')
        movies = self.user_active.movies.split(' ')
        inspired_by = self.user_active.inspired_by.split(' ')
        religion = self.user_active.religion.split(' ')
        if 'city' in receiving:
            if self.user_active.city == receiving['city']['title']:
                score += 30
        if 'bdate' in receiving:
            age = receiving['bdate'].split('.')
            number_of_elements = len(age)
            if number_of_elements == 3:
                now_date = datetime.datetime.now()
                birth_data = datetime.datetime(int(age[2]), int(age[1]), int(age[0]))
                age = (now_date - birth_data)
                age = int(age.days / 365)
                if self.user_active.age == age:
                    score += 30
            else:
                age = 'Возраст не указан'
        else:
            age = 'Возраст не указан'
        if 'relation' in receiving:
            if self.user_active.relation == receiving['relation']:
                score += 25
        if 'tv' in receiving:
            for tv_split in tv:
                if tv_split in receiving['tv']:
                    score += 2
        if 'quotes' in receiving:
            for quotes_split in quotes:
                if quotes_split in receiving['quotes']:
                    score += 2
        if 'interests' in receiving:
            for interests_split in interests:
                if interests_split in receiving['interests']:
                    score += 2
        if 'games' in receiving:
            for games_split in games:
                if games_split in receiving['games']:
                    score += 2
        if 'books' in receiving:
            for books_split in books:
                if books_split in receiving['books']:
                    score += 2
        if 'about' in receiving:
            for about_split in about:
                if about_split in receiving['about']:
                    score += 2
        if 'activities' in receiving:
            for activities_split in activities:
                if activities_split in receiving['activities']:
                    score += 2
        if 'music' in receiving:
            for music_split in music:
                if music_split in receiving['music']:
                    score += 2
        if 'movies' in receiving:
            for movies_split in movies:
                if movies_split in receiving['movies']:
                    score += 2
        if 'personal' in receiving:
            if 'alcohol' in receiving['personal']:
                if self.user_active.alcohol == receiving['personal']['alcohol']:
                    score += 15
        if 'personal' in receiving:
            if 'inspired_by' in receiving['personal']:
                for inspired_by_split in inspired_by:
                    if inspired_by_split in receiving['personal']['inspired_by']:
                        score += 2
        if 'personal' in receiving:
            if 'life_main' in receiving['personal']:
                if self.user_active.life_main == receiving['personal']['life_main']:
                    score += 10
        if 'personal' in receiving:
            if 'people_main' in receiving['personal']:
                if self.user_active.people_main == receiving['personal']['people_main']:
                    score += 10
        if 'personal' in receiving:
            if 'political' in receiving['personal']:
                if self.user_active.political == receiving['personal']['political']:
                    score += 10
        if 'personal' in receiving:
            if 'religion' in receiving['personal']:
                for religion_split in religion:
                    if religion_split in receiving['personal']['religion']:
                        score += 10
        if 'personal' in receiving:
            if 'smoking' in receiving['personal']:
                if self.user_active.smoking == receiving['personal']['smoking']:
                    score += 15
        if 'common_count' in receiving:
            score += 5 * receiving['common_count']

        return score, age

    def candidate_sorting(self, result_search, search):
        if 'response' in result_search:
            processing = result_search['response']['items']
        else:
            return
        id_list = []
        unsuccessful_search = 0
        for receiving in processing:
            id_candidate = receiving['id']
            result = self.database.select_candidate(self.user_active.user_id, id_candidate)
            if result is not None:
                continue
            result = self.database.select_blacklist(self.user_active.user_id, id_candidate)
            if result is not None:
                continue
            result = self.database.select_whitelist(self.user_active.user_id, id_candidate)
            if result is not None:
                continue
            score, age = search.evaluation_candidate(receiving)
            if score >= 60:
                self.database.insert_candidate(self.user_active.user_id, id_candidate)
                result_evaluations = search.photo_candidate(id_candidate, receiving['first_name'], age,
                                                            self.user_active.user_id, 'search', search)
                if result_evaluations == "0":
                    return "0"
                continue

            unsuccessful_search += 1
            new_id = {'id': id_candidate, 'score': score}
            id_list.append(new_id)
            if unsuccessful_search == 250:
                # когда счётчик доходит до 250, идёт выборка лучшего, на случай редкого подбора кандидатов
                applicant_list = []
                unsuccessful_search = 0
                id_list = sorted(id_list, key=itemgetter('score'))
                id_applicant = id_list[-1]['id']
                applicant_list.append(id_applicant)
                self.database.insert_candidate(self.user_active.user_id, id_candidate)
                result_evaluations = search.photo_candidate(id_candidate, receiving['first_name'], age,
                                                            self.user_active.user_id, 'search', search)
                if result_evaluations == "0":
                    return "0"

    def candidate_search(self, search):
        self.user_active.user_database(self.vk, self.bot_msg, self.long_poll, self.user_active, self.database)
        if self.user_active.age <= 1:
            age = 99
        else:
            age = self.user_active.age
        month = list(range(1, 13))
        random.shuffle(month)
        # Перемешиваем месяца в списке, чтобы при поиске январь не был всегда первым
        for birth_month in month:
            if birth_month in [1, 3, 5, 7, 8, 10, 12]:
                number_of_days = 32
            elif birth_month in [4, 6, 9, 11]:
                number_of_days = 31
            else:
                number_of_days = 30
            for birth_day in range(1, number_of_days):
                params = {
                    'count': 1000,
                    'birth_day': birth_day,
                    'birth_month': birth_month,
                    'age_to': age + 15,
                    'fields': 'first_name, sex, tv, quotes, personal, interests, games, books, about, activities, '
                              'music, movies, bdate, city, relation, common_count',
                    'sort': 0,
                    'sex': self.user_active.sex,
                }
                method = 'users.search'
                result_search = call_vk_method(method, params, self.user_active, self.vk_method_class, self.vk)
                reply = search.candidate_sorting(result_search, search)
                if reply == "0":
                    return "0"

    def status_candidate(self, id_candidate):
        params = {
            'user_id': id_candidate,
        }
        method = 'status.get'
        status_search = call_vk_method(method, params, self.user_active, self.vk_method_class, self.vk)
        if 'response' in status_search:
            pass
        else:
            return
        if 'text' in status_search['response']:
            status_search = status_search['response']['text']
        else:
            status_search = 'Нет статуса'
        return status_search

    def photo_candidate(self, id_candidate, name_candidate, age_candidate, id_user, operation, search):
        params = {
            'owner_id': id_candidate,
            'extended': 1,
            'offset': 0,
            'photo_sizes': 0,
            'no_service_albums': 0,
            'need_hidden': 0,
        }
        method = 'photos.getAll'
        photo_search = call_vk_method(method, params, self.user_active, self.vk_method_class, self.vk)
        photo_list = []
        try:
            photo_json_search = photo_search['response']['items']
        except KeyError:
            return
        else:
            photo_archive = []

            for photo in photo_json_search:
                new_key = {'id': photo['id'], 'likes': photo['likes']['count']}
                photo_archive.append(new_key)

            photo_archive = sorted(photo_archive, key=itemgetter('likes'))
            step = 0
            for photo in reversed(photo_archive):
                step += 1
                photo_list.append(photo['id'])
                if step >= 3:
                    break

            status_search = search.status_candidate(id_candidate)
            self.user_active.write_msg_photo(self.vk, id_candidate, photo_list, f"{name_candidate} {age_candidate}\n"
                                                                                f"{status_search}\n"
                                                                                f"https://vk.com/id{id_candidate}")
            if operation == 'whitelist':
                return

            self.user_active.write_msg(self.vk, self.bot_msg.user_opinion)
            for candidate_event in self.long_poll.listen():
                if candidate_event.type == VkEventType.MESSAGE_NEW and candidate_event.user_id == id_user:

                    if candidate_event.to_me:
                        request_choice = candidate_event.text
                        if request_choice == "1":
                            self.database.insert_whitelist(id_user, id_candidate)
                            self.user_active.write_msg(self.vk, f"Кандидат добавлен в избранное")
                            return request_choice
                        elif request_choice == "2":
                            self.database.insert_blacklist(id_user, id_candidate)
                            self.user_active.write_msg(self.vk, f"Кандидат добавлен в чёрный список")
                            return request_choice
                        elif request_choice == "3":
                            return request_choice
                        elif request_choice == "0":
                            return "0"
                        else:
                            self.user_active.write_msg(self.vk, self.bot_msg.user_opinion)
