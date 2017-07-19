from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    biography = models.TextField(max_length=500, blank=True)
    contacts = PhoneNumberField(blank=True, null=True,)
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


class ProfileChange(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    change_ip = models.CharField(max_length=20)
    change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Profile = {}, IP = {}, DATE = {}".format(self.profile, self.change_ip, self.change_date)
