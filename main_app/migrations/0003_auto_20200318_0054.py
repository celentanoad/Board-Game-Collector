# Generated by Django 3.0.2 on 2020-03-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200318_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='game',
            name='numPlayers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(max_length=250),
        ),
    ]
