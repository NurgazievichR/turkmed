from django.db import models

from apps.doctors.models import Doctor

class Appointment(models.Model):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),    
        )

    full_name = models.CharField('Полное имя', max_length=265)
    phone_number = models.CharField('Номер телефона', max_length=265)
    sex = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES)
    time = models.DateTimeField('Время')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Доктор', related_name='appointment_doctor')


    def __str__(self):
        return f"{self.full_name}-----{self.time}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Приём'
        verbose_name_plural = 'Приемы'
        

class AppointmentTime(models.Model):
    time = models.DateTimeField('Время')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Доктор', related_name='doctor_appointment_time')
    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT, verbose_name='Прием', null=True, blank=True)
    isAvailable = models.BooleanField(default=False, verbose_name='Зянато')

    def __str__(self):
        return f"{self.doctor}----{self.time}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Время приема'
        verbose_name = 'Время для приемов'




