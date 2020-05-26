from django.contrib import admin
from .models import Link, Motd, Member

# Register your models here.

admin.site.register(Link)
admin.site.register(Member)
admin.site.register(Motd)