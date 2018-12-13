from django.db import models
from django.utils import timezone
from martor.models import MartorField

class Summary(models.Model):
    summary = MartorField()

    def __str__(self):
        return self.summary
        #return mark_safe(markdown(self.summary, safe_mode='escape'))

    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    github_link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title

class Publication(models.Model):
    publication = models.CharField(max_length=200)

    def __str__(self):
        return self.publication

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
#    text = models.TextField()
    text = MartorField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Member(models.Model):
#    image = models.ImageField(upload_to='images/')
#    grade = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to='images/')
