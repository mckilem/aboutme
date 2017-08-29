import datetime
from mainapp.models import Skill
from mainapp.models import Work
from mainapp.models import Study
from mainapp.models import Hobby

class ClPersonalInfo:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.skills = []
        Skill.objects.all().delete()
        self.hobbies = []
        Hobby.objects.all().delete()
        self.studies = []
        Study.objects.all().delete()
        self.works = []
        Work.objects.all().delete()

    def __repr__(self):
        return str.format('{0}, Date of birth: {1}', self.name, self.date_of_birth)

    # def add_skill(self, skill):
    #     if not skill in self.skills:
    #         self.skills.append(skill)
    #
    # def add_skill(self, skill):
    #     if not skill in self.skills:
    #         self.skills.append(skill)
    #
    # #def add_study(self, name, image, alt_text, link):
    #     self.studies.append(ClStudy(name, image, alt_text, link))
    #
    # def add_work(self, name, image, alt_text, link):
    #     self.works.append(ClStudy(name, image, alt_text, link))

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
        list_of_skills = [
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

        self.skills = Skill.objects.all()
        if len(self.skills) == 0:
            for each_skill in list_of_skills:
                skill = Skill()
                skill.text = each_skill
                skill.save()
            self.skills = Skill.objects.all()

        list_of_hobbies = [
            'Из айтишного: ИИ, big data, deep machine learning, распознавание текста и образов',
            'Моделизм (клеить и пытаться красить)',
            'Стрельба из лука и страйкбол (сейчас уже реже)',
            'PS4 вечерком, поиграть в РПГ или какой-нибудь Dark Souls',
            'Dungeons & Dragons в роли мастера и игрока'
        ]

        self.hobbies = Hobby.objects.all()
        if len(self.hobbies) == 0:
            for each_hobby in list_of_hobbies:
                hobby = Hobby()
                hobby.text = each_hobby
                hobby.save()
            self.hobbies = Hobby.objects.all()

        self.studies = Study.objects.all()
        if len(self.studies) == 0:
            study = Study()
            study.organization = 'Гимназия №17'
            study.image_path = 'images/study/school.jpg'
            study.site = 'https://ru.wikipedia.org/wiki/Гимназия_№_17_(Пермь)'
            study.save()

            study = Study()
            study.organization = 'ПГНИУ'
            study.image_path = 'images/study/university.png'
            study.site = 'https://ru.wikipedia.org/wiki/Пермский_государственный_университет'
            study.save()

            study = Study()
            study.organization = 'GeekBrains.ru'
            study.image_path = 'images/study/gb.png'
            study.site = 'https://geekbrains.ru/'
            study.save()
        self.studies = Study.objects.all()

        self.works = Work.objects.all()
        if len(self.works) == 0:
            work = Work()
            work.organization = 'ПГНИУ'
            work.image_path = 'images/work/university.png'
            work.site = 'https://ru.wikipedia.org/wiki/Пермский_государственный_университет'
            work.save()

            work = Work()
            work.organization = 'ЗАО Прогноз'
            work.image_path = 'images/work/prognoz.jpeg'
            work.site = 'http://www.prognoz.ru/'
            work.save()
        self.works = Work.objects.all()

#
# class ClStudy:
#     def __init__(self, name, image_path, alt_text, link):
#         self.name = name
#         self.image_path = image_path
#         self.alt_text = alt_text
#         self.link = link
#
#     def __repr__(self):
#         return str.format('{0}, {1}, {2}, {3}', self.name, self.image_path, self.alt_text, self.link)
#
#
# class ClWork:
#     def __init__(self, name, image_path, alt_text, link):
#         self.name = name
#         self.image_path = image_path
#         self.alt_text = alt_text
#         self.link = link
#
#     def __repr__(self):
#         return str.format('{0}, {1}, {2}, {3}', self.name, self.image_path, self.alt_text, self.link)

