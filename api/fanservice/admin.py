from django.contrib import admin
from .models import User, Merchandise

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'favorite_team', 'favorite_driver')
    search_fields = ('name', 'email', 'favorite_team__name', 'favorite_driver__name')
    list_filter = ('favorite_team', 'favorite_driver')

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
