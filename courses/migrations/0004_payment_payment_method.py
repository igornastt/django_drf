# Generated by Django 4.2.5 on 2023-09-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_lesson_cours_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(default='перевод на счет', max_length=20, verbose_name='способ оплаты'),
        ),
    ]
    