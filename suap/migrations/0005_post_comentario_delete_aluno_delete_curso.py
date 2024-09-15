# Generated by Django 5.1 on 2024-08-24 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suap', '0004_curso_aluno_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo', models.TextField()),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='suap/')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suap.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]