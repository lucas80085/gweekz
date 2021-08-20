from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.fields import SlugField
from django.utils import translation




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



#Noah

class Game(models.Model):
    different_games = models.CharField(max_length=100)

    def __str__(self):
        return self.different_games

class Tag(models.Model):
   caption = models.CharField(max_length=30) 

   def __str__(self):
       return self.caption

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(null = True,max_length=20000)
    image = models.ImageField(null = True , blank = True)
    price = models.FloatField()
    games = models.ManyToManyField(Game)
    tags = models.ManyToManyField(Tag)
    slug = SlugField(unique= True)

    def __str__(self):
        return self.name
    #Render Images mit einer Model Methode um entweder das Image zu rendern oder ein leeren string, damit kein Error Code entsteht 

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ""
        return url


class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete= models.CASCADE)
    description = models.CharField(null = True,max_length=20000)
    email = models.CharField(max_length=200)
    image = models.ImageField(null = True , blank = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)

    def __str__(self):
     return self.user


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null =True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length= 100, null = True)
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    quantity = models.IntegerField(default=0, null = True , blank = True)
    date_added = models.DateTimeField(auto_now_add=True)
