# Generated by Django 4.0.3 on 2022-03-19 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_rename_professsor_module_professor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='module',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='professor',
        ),
    ]
