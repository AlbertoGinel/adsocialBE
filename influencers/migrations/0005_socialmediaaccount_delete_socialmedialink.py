# Generated by Django 5.1.4 on 2024-12-20 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0004_socialmedialink_username_alter_socialmedialink_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('twitter', 'Twitter'), ('youtube', 'YouTube'), ('tiktok', 'TikTok'), ('snapchat', 'Snapchat'), ('pinterest', 'Pinterest'), ('linkedin', 'LinkedIn'), ('reddit', 'Reddit'), ('whatsapp', 'WhatsApp'), ('tumblr', 'Tumblr'), ('twitch', 'Twitch'), ('vimeo', 'Vimeo'), ('spotify', 'Spotify'), ('clubhouse', 'Clubhouse'), ('medium', 'Medium'), ('periscope', 'Periscope'), ('wechat', 'WeChat'), ('viber', 'Viber'), ('discord', 'Discord'), ('line', 'Line'), ('telegram', 'Telegram'), ('tiktok_lite', 'TikTok Lite'), ('triller', 'Triller'), ('dlive', 'DLive'), ('myspace', 'MySpace'), ('google_plus', 'Google+'), ('yelp', 'Yelp'), ('musical_ly', 'Musical.ly'), ('vine', 'Vine')], max_length=50)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('social_media_account', models.URLField(unique=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('followers', models.PositiveIntegerField()),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_accounts', to='influencers.influencer')),
            ],
        ),
        migrations.DeleteModel(
            name='SocialMediaLink',
        ),
    ]
