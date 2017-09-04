import datetime
from mainapp.models import Skill
from mainapp.models import Work
from mainapp.models import Study
from mainapp.models import Hobby

class ClPersonalInfo:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.skills = Skill.objects.all()
        self.hobbies = Hobby.objects.all()
        self.studies = Study.objects.all()
        self.works = Work.objects.all()

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

