# Generated by Django 4.2 on 2024-12-28 14:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tem_message', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('message_body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='Sending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название рассылки')),
                ('time_first_mailing', models.DateTimeField(default=django.utils.datetime_safe.date.today, verbose_name='Дата первой рассылки')),
                ('periodicity', models.FloatField(verbose_name='Периодичность рассылки')),
                ('status', models.CharField(verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(to='client.client', verbose_name='Клиенты')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
