# Generated by Django 3.1.2 on 2020-11-18 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201118_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='exam_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='problemset',
            old_name='problemset_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='program_name',
            new_name='name',
        ),
    ]