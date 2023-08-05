from django.db import models

class Doctor(models.Model):
    image = models.ImageField('Фото', upload_to='doctor_images/')
    full_name = models.CharField('Полное имя', max_length=265)
    age = models.IntegerField('Возраст')
    job = models.CharField('Работа', max_length=265)
    phone_number = models.CharField('Номер телефона', max_length=265)
    description = models.TextField('Описание')

    def __str__(self):
        return f"{self.full_name}"
    
    class Meta: 
        ordering = ('-id',)
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'


class DoctorAward(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor_awards', on_delete=models.CASCADE, verbose_name='Доктор')
    image = models.ImageField('Фото',upload_to='doctor_awards/')

    def __str__(self):
        return f"{self.doctor.full_name}--------{self.id}"
        
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
    
