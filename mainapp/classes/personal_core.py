import datetime

class CLPersonalInfo:

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.skills = []
        self.hobbies = []

    def __repr__(self):
        return str.format('{0}, Date of birth: {1}', self.name, self.date_of_birth)

    def add_skill(self, skill):
        if not skill in self.skills:
            self.skills.append(skill)

    def add_skill(self, skill):
        if not skill in self.skills:
            self.skills.append(skill)

    def return_main_info_html(self): # todo хорошо ли так писать...
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
        self.date_of_birth = datetime.date(1988,6,8)
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
