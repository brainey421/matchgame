# Generated by Django 3.1.2 on 2020-10-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='date',
            field=models.DateField(),
        ),
    ]
