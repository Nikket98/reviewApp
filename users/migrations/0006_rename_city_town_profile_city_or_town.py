# Generated by Django 4.1.6 on 2023-04-13 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_security_answer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='city_town',
            new_name='city_or_town',
        ),
    ]