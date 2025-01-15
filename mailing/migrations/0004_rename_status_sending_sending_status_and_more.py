# Generated by Django 4.2 on 2025-01-15 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_alter_sending_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sending",
            old_name="status",
            new_name="sending_status",
        ),
        migrations.AlterField(
            model_name="sending",
            name="time_first_mailing",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Начало рассылки"
            ),
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата рассылки"
                    ),
                ),
                (
                    "status",
                    models.CharField(max_length=50, verbose_name="Статус рассылки"),
                ),
                ("service_response", models.TextField(verbose_name="Ответ почты")),
                (
                    "sending",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.sending",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус отправки",
                "verbose_name_plural": "Статусы отправки",
            },
        ),
    ]
