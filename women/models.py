
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from pytils.translit import slugify as slugify2
from text_unidecode import unidecode


class Women(models.Model):
    class Meta:
        verbose_name = 'Создать запись'
        verbose_name_plural = 'Создать записи'
        ordering = ['id']

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL(slug)', blank=True,unique=True)
    # {{old way}} content = models.TextField(blank=True,verbose_name='Текст статьи')
    content = RichTextUploadingField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    price = models.FloatField(verbose_name='Цена',blank=True, null=True,default=None)
    old_price = models.FloatField(blank=True, verbose_name='Старая цена (можно оставить пустым)', null=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    def save(self, *args, **kwargs):
        #* Если запись еще не сохранена в базе данных,
        #* создаем slug, добавляя случайное число
        base_slug = slugify2(self.title)
        slug = base_slug
        n = 1
        while Women.objects.filter(slug=slug).exists():
            slug = base_slug + '_' + str(n)
            n += 1
        self.slug = slug
        super(Women, self).save(*args, **kwargs)





class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL(slug)')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


 #class Profile(models.Model):
 #    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
 #    is_online = models.BooleanField(default=False)
 #    following = models.ManyToManyField(User, )
 #    friends = models.ManyToManyField(User, )
 #    bio = models.CharField(max_length=150, blank=True)
 #    image = models.ImageField('Аватар', upload_to='profile/')
 #    email_two = models.EmailField('Доп. Email')
 #    phone = models.CharField('Телефон', max_length=25)
 #    First_Name = models.CharField('Имя', max_length=25)
 #    Last_Name = models.CharField('Имя', max_length=25)
 #    date_of_birth = models.CharField(blank=True, max_length=150)
 #    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
 #    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
 #    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL(slug)', blank=True)
 ##
 #    def __str__(self):
 #        return self.First_Name
 #
 #    def save(self, *args, **kwargs):
 #        self.slug = slugify(self.First_Name)
 #        super(Profile, self).save(*args, **kwargs)
 #
 #    class Meta:
 #        verbose_name = "Профиль"
 #        verbose_name_plural = "Профиля"
 #
 #    # def profile_posts(self):
 #    #     return self.user.post_set.all()
 #
 #    def get_friends(self):
 #        return self.friends.all()
 #
 #    def get_friends_no(self):
 #        return self.friends.all().count()
 #
 #
 #STATUS_CHOICES = (
 #    ('send', 'send'),
 #    ('accepted', 'accepted')
 #)
 #
 #
 #class Relationship(models.Model):
 #    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_sender')
 #    reciever = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_reciever')
 #    status = models.CharField(max_length=9, choices=STATUS_CHOICES)
 #    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
 #    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
 #
 #    def __str__(self):
 #        return f'{self.sender} {self.reciever} {self.status}'
 ## @receiver(post_save, sender=User) хз
 ## def create_user_profile(sender,instanse,created,**kwargs):
 ##    if created:
 ##        Profile.objects.create(user=instanse)
 ##
 ## @receiver
 ## def save_user_profile(sender,instanse,**kwargs):
 ##    instanse.profile.save()
