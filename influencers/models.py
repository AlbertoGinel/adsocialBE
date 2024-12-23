from django.db import models

class Influencer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    manager = models.ForeignKey(
        'Manager', related_name='influencers', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SocialMediaAccount(models.Model):
    SOCIAL_NETWORK_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('snapchat', 'Snapchat'),
        ('pinterest', 'Pinterest'),
        ('linkedin', 'LinkedIn'),
        ('reddit', 'Reddit'),
        ('whatsapp', 'WhatsApp'),
        ('tumblr', 'Tumblr'),
        ('twitch', 'Twitch'),
        ('vimeo', 'Vimeo'),
        ('spotify', 'Spotify'),
        ('clubhouse', 'Clubhouse'),
        ('medium', 'Medium'),
        ('periscope', 'Periscope'),
        ('wechat', 'WeChat'),
        ('viber', 'Viber'),
        ('discord', 'Discord'),
        ('line', 'Line'),
        ('telegram', 'Telegram'),
        ('tiktok_lite', 'TikTok Lite'),
        ('triller', 'Triller'),
        ('dlive', 'DLive'),
        ('myspace', 'MySpace'),
        ('google_plus', 'Google+'),
        ('yelp', 'Yelp'),
        ('musical_ly', 'Musical.ly'),
        ('vine', 'Vine'),
    ]

    influencer = models.ForeignKey(
        Influencer,
        on_delete=models.CASCADE,
        related_name='social_media_accounts'
    )
    social_network = models.CharField(
        max_length=50,
        choices=SOCIAL_NETWORK_CHOICES
    )
    title = models.CharField(max_length=50, unique=True)
    account_url = models.URLField(unique=True)
    username = models.CharField(max_length=50, null=True)
    followers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.social_network}) - {self.influencer.first_name} {self.influencer.last_name}"


class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"