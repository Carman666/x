from django.db import models

# Create your models here.
class Book(models.Model):
    """如果没有定义主键，django里会自动定义增长的id
    id = models.AutoField(primary_key=True)"""
    name = models.CharField()
