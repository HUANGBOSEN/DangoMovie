from django.db import models

class User(models.Model):
    u_name=models.CharField(max_length=16)
    u_password=models.CharField(max_length=20)
    u_email=models.CharField(max_length=30)
    u_icon=models.ImageField(verbose_name='用户头像',upload_to='media')

class Movie(models.Model):
    m_postid= models.CharField(max_length=20)
    m_title=models.CharField(max_length=100)
    m_image=models.CharField(max_length=100)
    m_duration=models.CharField(max_length=30)
    m_app_fu_title=models.CharField(max_length=200)
    id_user=models.ManyToManyField(User)