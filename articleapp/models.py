from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # 어느 프로젝트(게시판)에 해당하는지 정보 추가
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    create_at = models.DateField(auto_created=True, null=True)