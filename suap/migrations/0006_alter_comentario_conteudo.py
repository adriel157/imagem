# Generated by Django 5.1 on 2024-08-24 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suap', '0005_post_comentario_delete_aluno_delete_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='conteudo',
            field=models.TextField(),
        ),
    ]
