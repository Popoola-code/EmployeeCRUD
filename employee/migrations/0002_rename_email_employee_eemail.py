# Generated by Django 3.2.9 on 2022-07-27 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='email',
            new_name='eemail',
        ),
    ]
