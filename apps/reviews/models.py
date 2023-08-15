from django.db import models

class Review(models.Model):
    full_name = models.CharField('Полное имя', max_length=265)
    description = models.CharField('Описание', max_length=1365)
    image = models.ImageField('Фото', upload_to='reviews/')
    create_at = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}---{self.create_at}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

        