from django.contrib import admin

from .models import Creator, Consumer, Customer, Order, OrderItem, Product, Tag, Game

from django.contrib import admin

class ConsumerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'avatar']

admin.site.register(Consumer, ConsumerAdmin)

class CreatorAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'avatar',
     'description']

admin.site.register(Creator, CreatorAdmin)


#admin.site.register(Profile)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Game)
