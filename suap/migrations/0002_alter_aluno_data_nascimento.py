# Generated by Django 5.1 on 2024-08-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]
