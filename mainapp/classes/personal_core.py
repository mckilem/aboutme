import datetime


class ClPersonalInfo:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.skills = []
        self.hobbies = []
        self.studies = []
        self.works = []

    def __repr__(self):
        return str.format('{0}, Date of birth: {1}', self.name, self.date_of_birth)

    def add_skill(self, skill):
        if not skill in self.skills:
            self.skills.append(skill)

    def add_skill(self, skill):
        if not skill in self.skills:
            self.skills.append(skill)

    def add_study(self, name, image, alt_text, link):
        self.studies.append(ClStudy(name, image, alt_text, link))

    def add_work(self, name, image, alt_text, link):
        self.works.append(ClStudy(name, image, alt_text, link))

    def return_main_info_html(self):  # todo хорошо ли так писать...
        html = \
            '<ul>' \
            '<li>' \
            + self.name + \
            '</li>' \
            '<li>' \
            + self.date_of_birth + \
            '</li>' \
            '</ul>'

    def init_defaults(self):
        self.name = 'Георгий'
        self.date_of_birth = datetime.date(1988, 6, 8)
        self.skills = [
            'Математика во всех ее проявлениях, все таки магистратуру мехмата осилил;',
            'Нейросети. Люблю нейросети.',
            'ООП, куда же без него',
            'Алгоритмическое мышление - есть',
            'HTML5/CSS3 - ну, учил :)',
            'JavaScript - совсем поверхностно :(',
            'С# - тут намного лучше',
            'SQL - \"могу писать сложные запросы\"',
            'Проектирование приложений',
            'Проектирование баз данных',
            'Python',
            'Git, Jira, TFS, Redmine'
        ]

        self.hobbies = [
            'Из айтишного: ИИ, big data, deep machine learning, распознавание текста и образов',
            'Моделизм (клеить и пытаться красить)',
            'Стрельба из лука и страйкбол (сейчас уже реже)',
            'PS4 вечерком, поиграть в РПГ или какой-нибудь Dark Souls',
            'Dungeons & Dragons в роли мастера и игрока'
        ]

        self.add_study('Гимназия №17', 'images/study/school.jpg', 'школа', 'https://ru.wikipedia.org/wiki/'
                                                                           'Гимназия_№_17_(Пермь)')
        self.add_study('ПГНИУ', 'images/study/university.png', 'ПГНИУ', 'https://ru.wikipedia.org/wiki/Пермский_'
                                                                        'государственный_университет')
        self.add_study('GeekBrains.ru', 'images/study/gb.png', 'geekbrains logo', 'https://geekbrains.ru/')

        self.add_work('ПГНИУ', 'images/work/university.png', 'ПГНИУ', 'https://ru.wikipedia.org/wiki/Пермский_'
                                                                      'государственный_университет')
        self.add_work('ЗАО Прогноз', 'images/work/prognoz.jpeg', 'prognoz logo', 'http://www.prognoz.ru/')


class ClStudy:
    def __init__(self, name, image_path, alt_text, link):
        self.name = name
        self.image_path = image_path
        self.alt_text = alt_text
        self.link = link

    def __repr__(self):
        return str.format('{0}, {1}, {2}, {3}', self.name, self.image_path, self.alt_text, self.link)


class ClWork:
    def __init__(self, name, image_path, alt_text, link):
        self.name = name
        self.image_path = image_path
        self.alt_text = alt_text
        self.link = link

    def __repr__(self):
        return str.format('{0}, {1}, {2}, {3}', self.name, self.image_path, self.alt_text, self.link)
