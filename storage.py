import psycopg2
import psycopg2.extras


class WorkingDatabase:
    def __init__(self, dbname, user_bd, password):
        self.connection = psycopg2.connect(f"dbname={dbname} user={user_bd} password={password}")
        self.connection.autocommit = True
        self.operations = self.connection.cursor()
        self.dict_cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def insert_data_user(self, user_active):
        self.operations.execute('''INSERT INTO user_finder (id_user, first_name, sex, age_user, city, relation, tv, 
        quotes, interests, games, books, about, activities, music, movies, alcohol, inspired_by, life_main, 
        people_main, political, religion, smoking) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                                (user_active.user_id, user_active.first_name, user_active.sex, user_active.age,
                                 user_active.city, user_active.relation, user_active.tv, user_active.quotes,
                                 user_active.interests, user_active.games, user_active.books, user_active.about,
                                 user_active.activities, user_active.music, user_active.movies, user_active.alcohol,
                                 user_active.inspired_by, user_active.life_main, user_active.people_main,
                                 user_active.political, user_active.religion, user_active.smoking,))

    def insert_candidate(self, id_user, id_candidate):
        self.operations.execute("INSERT INTO communications (user_finder_id, search_results_id) values(%s, %s)",
                                (id_user, id_candidate,))

    def insert_whitelist(self, id_user, id_candidate):
        self.operations.execute(
            "INSERT INTO whitelist (user_finder_id, search_results_id) values(%s, %s)",
            (id_user, id_candidate,))

    def insert_blacklist(self, id_user, id_candidate):
        self.operations.execute(
            "INSERT INTO blacklist (user_finder_id, search_results_id) values(%s, %s)",
            (id_user, id_candidate,))

    def select_user_id(self, id_user):
        self.operations.execute("SELECT id_user, first_name FROM user_finder WHERE id_user = %s", (id_user,))
        return self.operations.fetchone()

    def select_full_data(self, id_user):
        self.dict_cur.execute("SELECT id_user, first_name, sex, age_user, city, relation, tv, quotes, interests, "
                              "games, books, about, activities, music, movies, alcohol, inspired_by, life_main, "
                              "people_main, political, religion, smoking FROM user_finder "
                              "WHERE id_user = %s", (id_user,))
        rec = self.dict_cur.fetchone()
        return rec

    def select_whitelist(self, id_user, id_candidate):
        self.operations.execute("SELECT user_finder_id, search_results_id FROM whitelist "
                                "WHERE user_finder_id = %s AND search_results_id = %s",
                                (id_user, id_candidate,))
        return self.operations.fetchone()

    def select_blacklist(self, id_user, id_candidate):
        self.operations.execute("SELECT user_finder_id, search_results_id FROM blacklist "
                                "WHERE user_finder_id = %s AND search_results_id = %s", (id_user, id_candidate,))
        return self.operations.fetchone()

    def select_candidate(self, id_user, id_candidate):
        self.operations.execute("SELECT user_finder_id, search_results_id FROM communications "
                                "WHERE user_finder_id = %s AND search_results_id = %s", (id_user, id_candidate,))
        return self.operations.fetchone()

    def select_full_whitelist(self, id_user):
        self.operations.execute("SELECT search_results_id FROM whitelist WHERE user_finder_id = %s", (id_user,))
        return self.operations.fetchone()

    def select_full_blacklist(self, id_user):
        self.operations.execute("SELECT search_results_id FROM blacklist WHERE user_finder_id = %s", (id_user,))
        return self.operations.fetchone()

    def select_full_token(self, id_user):
        self.operations.execute("SELECT token_user FROM user_finder WHERE id_user = %s", (id_user,))
        return self.operations.fetchone()

    def update_data_user(self, user_active):
        self.operations.execute('''UPDATE user_finder SET (first_name, sex, age_user, city, relation, tv, quotes, 
        interests, games, books, about, activities, music, movies, alcohol, inspired_by, life_main, people_main, 
        political, religion, smoking) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, 
        %s, %s, %s) WHERE id_user = %s''',
                                (user_active.first_name, user_active.sex, user_active.age,
                                 user_active.city, user_active.relation, user_active.tv, user_active.quotes,
                                 user_active.interests, user_active.games, user_active.books, user_active.about,
                                 user_active.activities, user_active.music, user_active.movies, user_active.alcohol,
                                 user_active.inspired_by, user_active.life_main, user_active.people_main,
                                 user_active.political, user_active.religion, user_active.smoking,
                                 user_active.user_id,))

    def update_sex(self, id_user, sex):
        self.operations.execute("UPDATE user_finder SET sex = %s WHERE id_user = %s",
                                (sex, id_user,))

    def update_age_user(self, id_user, age):
        self.operations.execute("UPDATE user_finder SET age_user = %s WHERE id_user = %s",
                                (age, id_user,))

    def update_city(self, id_user, city):
        self.operations.execute("UPDATE user_finder SET city = %s WHERE id_user = %s",
                                (city, id_user,))

    def update_relation(self, id_user, relation):
        self.operations.execute("UPDATE user_finder SET relation = %s WHERE id_user = %s",
                                (relation, id_user,))

    def update_tv(self, id_user, tv):
        self.operations.execute("UPDATE user_finder SET tv = %s WHERE id_user = %s",
                                (tv, id_user,))

    def update_quotes(self, id_user, quotes):
        self.operations.execute("UPDATE user_finder SET quotes = %s WHERE id_user = %s",
                                (quotes, id_user,))

    def update_interests(self, id_user, interests):
        self.operations.execute("UPDATE user_finder SET interests = %s WHERE id_user = %s",
                                (interests, id_user,))

    def update_games(self, id_user, games):
        self.operations.execute("UPDATE user_finder SET games = %s WHERE id_user = %s",
                                (games, id_user,))

    def update_books(self, id_user, books):
        self.operations.execute("UPDATE user_finder SET books = %s WHERE id_user = %s",
                                (books, id_user,))

    def update_about(self, id_user, about):
        self.operations.execute("UPDATE user_finder SET about = %s WHERE id_user = %s",
                                (about, id_user,))

    def update_activities(self, id_user, activities):
        self.operations.execute("UPDATE user_finder SET activities = %s WHERE id_user = %s",
                                (activities, id_user,))

    def update_music(self, id_user, music):
        self.operations.execute("UPDATE user_finder SET music = %s WHERE id_user = %s",
                                (music, id_user,))

    def update_movies(self, id_user, movies):
        self.operations.execute("UPDATE user_finder SET movies = %s WHERE id_user = %s",
                                (movies, id_user,))

    def update_alcohol(self, id_user, alcohol):
        self.operations.execute("UPDATE user_finder SET alcohol = %s WHERE id_user = %s",
                                (alcohol, id_user,))

    def update_inspired_by(self, id_user, inspired_by):
        self.operations.execute("UPDATE user_finder SET inspired_by = %s WHERE id_user = %s",
                                (inspired_by, id_user,))

    def update_life_main(self, id_user, life_main):
        self.operations.execute("UPDATE user_finder SET life_main = %s WHERE id_user = %s",
                                (life_main, id_user,))

    def update_people_main(self, id_user, people_main):
        self.operations.execute("UPDATE user_finder SET people_main = %s WHERE id_user = %s",
                                (people_main, id_user,))

    def update_political(self, id_user, political):
        self.operations.execute("UPDATE user_finder SET political = %s WHERE id_user = %s",
                                (political, id_user,))

    def update_religion(self, id_user, religion):
        self.operations.execute("UPDATE user_finder SET religion = %s WHERE id_user = %s",
                                (religion, id_user,))

    def update_smoking(self, id_user, smoking):
        self.operations.execute("UPDATE user_finder SET smoking = %s WHERE id_user = %s",
                                (smoking, id_user,))

    def update_token(self, id_user, token_user_update):
        self.operations.execute("UPDATE user_finder SET token_user = %s WHERE id_user = %s",
                                (token_user_update, id_user,))

    def delete_search_history(self, id_user):
        self.operations.execute("DELETE FROM communications WHERE user_finder_id = %s", (id_user,))

    def delete_whitelist(self, id_user, search_results_id):
        self.operations.execute("DELETE FROM whitelist WHERE user_finder_id = %s AND search_results_id = %s",
                                (id_user, search_results_id))

    def delete_blacklist(self, id_user, search_results_id):
        self.operations.execute("DELETE FROM blacklist WHERE user_finder_id = %s AND search_results_id = %s",
                                (id_user, search_results_id))

    def operations_fetchone(self):
        result = self.operations.fetchone()
        return result
