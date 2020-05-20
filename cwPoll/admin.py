from django.contrib import admin
from .models import Poll,Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ['pollDescription', 'pollInDetail'],
        }),
        ('Date info', {
            "fields": ['pollDate'],
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('pollDescription', 'pollDate', 'isRecent')

    
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)