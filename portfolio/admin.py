from django.db import models
from django.contrib import admin
from martor.widgets import AdminMartorWidget
from .models import Summary, Project, Publication, Member, Post, Gallery

class SummaryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

class TextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Summary, SummaryAdmin)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Member)
admin.site.register(Post, TextAdmin)
admin.site.register(Gallery)
