# Generated by Django 4.0.3 on 2022-03-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='professsor',
        ),
        migrations.AddField(
            model_name='module',
            name='professsor',
            field=models.ManyToManyField(to='rating.professor'),
        ),
    ]