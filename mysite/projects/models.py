from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField

# Create your models here.
SKILL_CHOICES = (
        ('android', "Android Developer"),
        ('designer', "Designer"),
        ('java', "Java Developer"),
        ('php', "PHP Developer"),
        ('python', "Python Developer"),
        ('rails', "Rails Developer"),
        ('wordpress', "Wordpress Devloper"),
        ('ios', "iOS Developer")
    )


class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=35, default='')
    description = models.TextField(default='')
    requirements = models.TextField(default='')
    timeline = models.TextField(default='')
    skills = MultiSelectField(choices=SKILL_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'project_pk': self.id})


class Position(models.Model):
    project = models.ForeignKey(Project, default='', related_name='positions')
    name = models.CharField(max_length=35, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Application(models.Model):
    APP_STATUS = (
        ('p', 'Pending'),
        ('a', 'Accepted'),
        ('r', 'Rejected'),
    )
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    status = models.CharField(max_length=1, choices=APP_STATUS, default='p')