# Generated by Django 2.1.5 on 2019-01-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190127_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
    ]
