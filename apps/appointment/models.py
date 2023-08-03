from django.db import models

class Appointment(models.Model):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),    
        )

    full_name = models.CharField('Полное имя', max_length=265)
    phone_number = models.CharField('Номер телефона', max_length=265)
    sex = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES)
    time = models.TimeField('Время', auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}-----{self.time}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'
        


