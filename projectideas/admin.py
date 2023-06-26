from django.contrib import admin
from .models import Course, Technology, Project_ideas

# Register your models here.
admin.site.register(Course)
admin.site.register(Technology)
admin.site.register(Project_ideas)
