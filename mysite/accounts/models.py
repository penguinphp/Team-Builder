from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='images/', blank=True)
    skills = MultiSelectField(choices=SKILL_CHOICES)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


