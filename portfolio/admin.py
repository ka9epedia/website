from django.db import models
from django.contrib import admin
from martor.widgets import AdminMartorWidget
from .models import Degree, Skill, Summary, Project, Publication, Members

class SummaryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Summary, SummaryAdmin)
admin.site.register(Skill)
admin.site.register(Degree)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Members)
