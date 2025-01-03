# Generated by Django 5.1.4 on 2024-12-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0003_manager_influencer_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedialink',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='link',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
