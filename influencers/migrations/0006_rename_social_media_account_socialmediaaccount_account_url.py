# Generated by Django 5.1.4 on 2024-12-20 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0005_socialmediaaccount_delete_socialmedialink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmediaaccount',
            old_name='social_media_account',
            new_name='account_url',
        ),
    ]
