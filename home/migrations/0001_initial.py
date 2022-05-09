# Generated by Django 4.0.4 on 2022-05-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Емаил')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('active', models.BooleanField(default=True, verbose_name='В работе')),
            ],
            options={
                'verbose_name': 'Обращение гражданина',
                'verbose_name_plural': 'Обращения граждан',
                'db_table': 'feedback',
                'unique_together': {('full_name', 'email', 'active')},
            },
        ),
    ]
