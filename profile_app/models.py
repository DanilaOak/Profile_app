from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# first name, last name, data of birth, biography,contacts
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    biography = models.TextField(max_length=500, blank=True)
    contacts = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def to_dict(self):
        dictionary = {"User Name": self.user.username,
                      "First Name": self.first_name,
                      "Last Name": self.last_name,
                      "Email": self.email,
                      "Biography": self.biography,
                      "Contacts": self.contacts,
                      "Data of birth": self.birth_date,
                      }
        return dictionary

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
