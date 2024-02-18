from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class PublishMan(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)
class Cars(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m%d',default=None, blank=True,null=True,verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус')
    cat = models.ForeignKey('Categories',on_delete=models.PROTECT, verbose_name='Категории')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,related_name='posts', null=True,default=None)
    objects = models.Manager()
    published = PublishMan()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={ 'post_slug': self.slug})

class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True,db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('category', kwargs={'cat_slug': self.slug})

class UploadF(models.Model):
    file = models.FileField(upload_to='uploads_model')

class AddContact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name