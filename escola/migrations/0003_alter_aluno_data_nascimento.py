# Generated by Django 3.2 on 2022-08-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_auto_20220821_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]
