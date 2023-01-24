from dataclasses import dataclass
import datetime
from random import randrange
from vk_api.longpoll import VkEventType


@dataclass
class UserVkTinder:
    user_id: int = 0
    first_name: str = ''
    sex: int = 0
    age: int = 0
    city: str = ''
    relation: int = 0
    tv: str = ''
    quotes: str = ''
    interests: str = ''
    games: str = ''
    books: str = ''
    about: str = ''
    activities: str = ''
    music: str = ''
    movies: str = ''
    alcohol: int = 0
    inspired_by: str = ''
    life_main: int = 0
    people_main: int = 0
    political: int = 0
    religion: str = ''
    smoking: int = 0

    def full_user_data(self, user_id, data):
        self.user_id = user_id
        self.first_name = data[0]['first_name']
        if 'bdate' in data[0]:
            age = data[0]['bdate'].split('.')
            number_of_elements = len(age)
            if number_of_elements == 3:
                now_date = datetime.datetime.now()
                birth_data = datetime.datetime(int(age[2]), int(age[1]), int(age[0]))
                age = (now_date - birth_data)
                age = int(age.days / 365)
            else:
                age = 20
        else:
            age = 20
        self.age = age
        if 'city' in data[0]:
            city = data[0]['city']['title']
        else:
            city = '0'
        self.city = city
        gender = data[0]['sex']
        if gender == 1:
            gender = 2
        else:
            gender = 1
        self.sex = gender
        if 'relation' in data[0]:
            relation = data[0]['relation']
        else:
            relation = 0
        self.relation = relation
        if 'interests' in data[0]:
            interests = data[0]['interests']
        else:
            interests = '-1'
        self.interests = interests
        if 'books' in data[0]:
            books = data[0]['books']
        else:
            books = '-1'
        self.books = books
        if 'tv' in data[0]:
            tv = data[0]['tv']
        else:
            tv = '-1'
        self.tv = tv
        if 'quotes' in data[0]:
            quotes = data[0]['quotes']
        else:
            quotes = '-1'
        self.quotes = quotes
        if 'about' in data[0]:
            about = data[0]['about']
        else:
            about = '-1'
        self.about = about
        if 'games' in data[0]:
            games = data[0]['games']
        else:
            games = '-1'
        self.games = games
        if 'movies' in data[0]:
            movies = data[0]['movies']
        else:
            movies = '-1'
        self.movies = movies
        if 'activities' in data[0]:
            activities = data[0]['activities']
        else:
            activities = '-1'
        self.activities = activities
        if 'music' in data[0]:
            music = data[0]['music']
        else:
            music = '-1'
        self.music = music
        if 'personal' in data[0]:
            if 'alcohol' in data[0]['personal']:
                alcohol = data[0]['personal']['alcohol']
            else:
                alcohol = 0
            self.alcohol = alcohol
        if 'personal' in data[0]:
            if 'inspired_by' in data[0]['personal']:
                inspired_by = data[0]['personal']['inspired_by']
            else:
                inspired_by = '-1'
            self.inspired_by = inspired_by
        if 'personal' in data[0]:
            if 'life_main' in data[0]['personal']:
                life_main = data[0]['personal']['life_main']
            else:
                life_main = 0
            self.life_main = life_main
        if 'personal' in data[0]:
            if 'people_main' in data[0]['personal']:
                people_main = data[0]['personal']['people_main']
            else:
                people_main = 0
            self.people_main = people_main
        if 'personal' in data[0]:
            if 'political' in data[0]['personal']:
                political = data[0]['personal']['political']
            else:
                political = 0
            self.political = political
        if 'personal' in data[0]:
            if 'religion' in data[0]['personal']:
                religion = data[0]['personal']['religion']
            else:
                religion = '-1'
            self.religion = religion
        if 'personal' in data[0]:
            if 'smoking' in data[0]['personal']:
                smoking = data[0]['personal']['smoking']
            else:
                smoking = 0
            self.smoking = smoking

        return

    def import_full_data(self, result):
        self.user_id = result['id_user']
        self.first_name = result['first_name']
        self.sex = result['sex']
        self.age = result['age_user']
        self.city = result['city']
        self.relation = result['relation']
        self.tv = result['tv']
        self.quotes = result['quotes']
        self.interests = result['interests']
        self.games = result['games']
        self.books = result['books']
        self.about = result['about']
        self.activities = result['activities']
        self.music = result['music']
        self.movies = result['movies']
        self.alcohol = result['alcohol']
        self.inspired_by = result['inspired_by']
        self.life_main = result['life_main']
        self.people_main = result['people_main']
        self.political = result['political']
        self.religion = result['religion']
        self.smoking = result['smoking']
        return

    def user_database(self, vk, bot_msg, long_poll, user_active, database):
        result = database.select_full_data(self.user_id)
        if result[3] <= 0:
            user_active.write_msg(vk, f"Не указан возраст, укажите свой возраст или введите 99, чтобы этот вопрос "
                                      f"больше не возникал для {self.user_id}")
            for age_event in long_poll.listen():
                if age_event.type == VkEventType.MESSAGE_NEW and age_event.user_id == self.user_id:

                    if age_event.to_me:
                        request_age = age_event.text
                        try:
                            age = int(request_age)
                            database.update_age_user(self.user_id, age)
                            user_active.age = age
                            break
                        except ValueError:
                            user_active.write_msg(vk, f"Возраст не задан для {self.user_id}")
                            break
        if result[4] == '0':
            user_active.write_msg(vk, f"Не указан город, укажите название своего города или введите -1, "
                                      f"чтобы этот вопрос больше не возникал для {self.user_id}")
            for city_event in long_poll.listen():
                if city_event.type == VkEventType.MESSAGE_NEW and city_event.user_id == self.user_id:
                    if city_event.to_me:
                        request_city = city_event.text
                        try:
                            city = request_city
                            database.update_city(self.user_id, city)
                            user_active.city = city
                            break
                        except ValueError:
                            user_active.write_msg(vk, f"Город не указан для {self.user_id}")
                            break
        if result[5] == 0:
            user_active.write_msg(vk, f"Не указано семейное положение, введите:\n {bot_msg.marital_status} "
                                      f"-1, чтобы этот вопрос больше не возникал для {self.user_id}")
            for relation_event in long_poll.listen():
                if relation_event.type == VkEventType.MESSAGE_NEW and relation_event.user_id == self.user_id:
                    if relation_event.to_me:
                        request_relation_event = relation_event.text
                        try:
                            relation = int(request_relation_event)
                            database.update_relation(self.user_id, relation)
                            user_active.relation = relation
                            break
                        except ValueError:
                            user_active.write_msg(vk, f"Семейное положение, не задан для {self.user_id}")
                            break

        result = database.select_full_data(self.user_id)
        return result

    def write_msg(self, vk, message):
        vk.method('messages.send', {'user_id': self.user_id, 'message': message, 'random_id': randrange(10 ** 7)})

    def write_msg_photo(self, vk, result, photo_list, message):
        photo_id = ''
        for photo in photo_list:
            if len(photo_id) != 0:
                photo_id += ','
            photo_id += 'photo' + str(result) + '_' + str(photo)
        if len(photo_id) == 0:
            message += '\nНа аккаунте нет фотографий'
        vk.method('messages.send', {'user_id': self.user_id, 'message': message, 'attachment': photo_id,
                                    'random_id': randrange(10 ** 7)})
        return
