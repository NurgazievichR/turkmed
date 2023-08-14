from django.db import models

class New(models.Model):
    title = models.CharField('Название', max_length=265)
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='news_photos')
    date = models.DateField('Дата', auto_now_add=True)
    time = models.TimeField('Время', auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class License(models.Model):
    title = models.CharField('Название', max_length=265)
    image = models.ImageField('Фото', upload_to='license/')

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

class Gallery(models.Model):
    title = models.CharField('Название', max_length=265, null=True, blank=True)
    image = models.ImageField('Фото', upload_to='gallery/')

    def __str__(self):
        return f"{self.image.path}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Фото для галлереи'
        verbose_name_plural = 'Фотографии для галлереи'


