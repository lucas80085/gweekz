from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        CONSUMER = "CONSUMER", "Consumer"
        CREATOR = "CREATOR", "Creator"

    base_type = Types.CONSUMER

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    first_name = models.CharField(_("first name"), max_length=50, default="")
    last_name = models.CharField(_("last name"), max_length=50, default="")
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("username"), max_length=50, unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(default='dafault.jpg', upload_to='media/avatar')

    


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class ConsumerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CONSUMER)


class CreatorManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CREATOR)



class Consumer(User):
    type = User.Types.CONSUMER

    objects = ConsumerManager()



class Creator(User):
    type = User.Types.CREATOR

    description = models.TextField(max_length=500, default="")
    
    objects = CreatorManager()

    class Meta:
        verbose_name = "Creator"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
