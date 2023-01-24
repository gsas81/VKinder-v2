class AppConfig:
    def __init__(self):
        self.dbname = ''
        self.user_bd = ''
        self.password = ''
        self.token = ''
        self.application_access_link = ''

    def input_data(self):
        self.dbname = input('Ведите название базы данных: ')
        self.user_bd = input('Введите пользователя базы данных: ')
        self.password = input('Введите пароль пользователя базы данных: ')
        self.token = input('Введите токен чат-бота: ')
        client_id = str(input('Введите ID приложения: '))
        # ID приложения из ВК
        application_access = 'https://oauth.vk.com/authorize?client_id=' + client_id
        application_access = application_access + '&display=popup&redirect_uri=https://oauth.vk.com/'
        self.application_access_link = application_access + 'blank.html&scope=friends,status,photos,' \
                                                            'offline&response_type=token&v=5.131'
