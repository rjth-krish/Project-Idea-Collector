from django.db import models
from django.contrib.auth.models import User

# Create your models here.
project_type = (
    (0, 'mini project'),
    (1, 'main project'),
    (2, 'live project'),
)


class Master(models.Model):
    created_user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Course(Master):
    course = models.CharField(max_length=220)

    def __str__(self):
        return self.course

    class Meta:
        verbose_name_plural = 'Courses'


class Technology(Master):
    technology = models.CharField(max_length=220)

    def __str__(self):
        return self.technology

    class Meta:
        verbose_name_plural = 'Technologies'


class Project_ideas(Master):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    project_type = models.IntegerField(choices=project_type, null=False)
    description = models.TextField()
    technology = models.ManyToManyField(Technology, blank=True)
    project_title = models.CharField(max_length=220)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name_plural = 'Project_ideas'
