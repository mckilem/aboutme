from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Work, Hobby, Study, Organization, Skill
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        organizations = [
            {'name': 'ПГНИУ', 'image_path': 'images/work/university.png', 'site': 'https://ru.wikipedia.org/wiki/Пермский_государственный_университет'},
            {'name': 'ЗАО Прогноз', 'image_path': 'images/work/prognoz.jpeg', 'site': 'http://www.prognoz.ru/'},
        ]

        works = [
            {'organization': 'ПГНИУ', 'position': 'Администратор', 'duties': 'Поддержка серверов'},
            {'organization': 'ЗАО Прогноз', 'position': 'Программист', 'duties': 'Написание кода'},
        ]

        studies = [
            {'name': 'Гимназия №17', 'image_path': 'images/study/school.jpg', 'site': 'https://ru.wikipedia.org/wiki/Гимназия_№_17_(Пермь)'},
            {'name': 'ПГНИУ', 'image_path': 'images/study/university.png', 'site': 'https://ru.wikipedia.org/wiki/Пермский_государственный_университет'},
            {'name': 'GeekBrains.ru', 'image_path': 'images/study/gb.png', 'site': 'https://geekbrains.ru/'},
        ]

        skills = [
            {'text': 'Математика во всех ее проявлениях, все таки магистратуру мехмата осилил'},
            {'text': 'Нейросети. Люблю нейросети.'},
            {'text': 'ООП, куда же без него'},
            {'text': 'Алгоритмическое мышление - есть'},
            {'text': 'HTML5/CSS3 - ну, учил :)'},
            {'text': 'JavaScript - совсем поверхностно :('},
            {'text': 'С# - тут намного лучше'},
            {'text': 'SQL - \"могу писать сложные запросы\"'},
            {'text': 'Проектирование приложений'},
            {'text': 'Проектирование баз данных',},
            {'text': 'Python'},
            {'text': 'Git, Jira, TFS, Redmine'},
        ]

        hobbies = [
            {'text': 'Из айтишного: ИИ, big data, deep machine learning, распознавание текста и образов'},
            {'text': 'Моделизм (клеить и пытаться красить)'},
            {'text': 'Стрельба из лука и страйкбол (сейчас уже реже)'},
            {'text': 'PS4 вечерком, поиграть в РПГ или какой-нибудь Dark Souls'},
            {'text': 'Dungeons & Dragons в роли мастера и игрока'},
        ]

        Organization.objects.all().delete()
        Work.objects.all().delete()
        Hobby.objects.all().delete()
        Study.objects.all().delete()
        Skill.objects.all().delete()

        for organization in organizations:
            organization = Organization(**organization)
            organization.save()
        for work in works:
            org_name = work["organization"]
            # Получаем организацию по имени
            organization = Organization.objects.get(name=org_name)
            # Заменяем название организации объектом
            work['organization'] = organization
            work = Work(**work)
            work.save()
        for hobby in hobbies:
            hobby = Hobby(**hobby)
            hobby.save()
        for study in studies:
            study = Study(**study)
            study.save()
        for skill in skills:
            skill = Skill(**skill)
            skill.save()