# Generated by Django 4.2.5 on 2023-09-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='изображение')),
                ('description', models.TextField(max_length=500, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='изображение')),
                ('description', models.TextField(max_length=500, verbose_name='описание')),
                ('link', models.URLField(blank=True, null=True, verbose_name='ссылка на видео')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
