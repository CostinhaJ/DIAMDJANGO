# Generated by Django 5.0.3 on 2024-03-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0003_aluno_votosfeitos'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='grupo',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
