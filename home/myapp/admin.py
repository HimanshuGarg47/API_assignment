from django.contrib import admin
from .models import Work, Artist, Client, Rating

admin.site.register(Work)
admin.site.register(Artist)
admin.site.register(Client)
admin.site.register(Rating)