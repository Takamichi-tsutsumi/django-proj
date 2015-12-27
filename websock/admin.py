from django.contrib import admin
from websock.models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'point')
    list_display_links = ('title', )
admin.site.register(Subject, SubjectAdmin)
