from django.contrib import admin

from .models import Creator, Consumer#, Profile

class ConsumerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'avatar']

admin.site.register(Consumer, ConsumerAdmin)

class CreatorAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'avatar',
     'description']

admin.site.register(Creator, CreatorAdmin)


#admin.site.register(Profile)
