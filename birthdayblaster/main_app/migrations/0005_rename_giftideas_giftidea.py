# Generated by Django 4.2.5 on 2023-09-18 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_birthday_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GiftIdeas',
            new_name='GiftIdea',
        ),
    ]
