from django.db import models
from django.utils.datetime_safe import date

from client.models import Client


class Message(models.Model):

    tem_message = models.CharField(max_length=100, verbose_name='Тема письма')
    message_body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.tem_message}'

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"


class Sending(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название рассылки")
    time_first_mailing = models.DateTimeField(default=date.today, verbose_name="Дата первой рассылки")
    periodicity = models.FloatField(verbose_name="Периодичность рассылки")
    status = models.CharField(verbose_name="Статус рассылки")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


