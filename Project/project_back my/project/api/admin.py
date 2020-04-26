from django.contrib import admin
from .models import Category, Game, Company, User

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Company)
admin.site.register(User)
