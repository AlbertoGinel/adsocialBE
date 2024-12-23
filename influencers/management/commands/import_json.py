import json
from django.core.management.base import BaseCommand
from influencers.models import Influencer, SocialMediaAccount, Manager

class Command(BaseCommand):
    help = 'Populate the database with data from a JSON file'

    def handle(self, *args, **kwargs):
        # Load JSON data from file
        with open('data.json', 'r') as file:
            data = json.load(file)

        # Insert managers
        for manager_data in data['managers']:
            manager, created = Manager.objects.get_or_create(
                first_name=manager_data['first_name'],
                last_name=manager_data['last_name']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created manager: {manager.first_name} {manager.last_name}'))

        # Insert influencers
        for influencer_data in data['influencers']:
            manager_name = influencer_data['manager_name']
            manager = Manager.objects.get(first_name=influencer_data['manager_name'].split()[0],
                                          last_name=influencer_data['manager_name'].split()[1])

            influencer, created = Influencer.objects.get_or_create(
                first_name=influencer_data['first_name'],
                last_name=influencer_data['last_name'],
                manager=manager
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created influencer: {influencer.first_name} {influencer.last_name}'))

            # Insert social media accounts
            for account_data in influencer_data['social_media_accounts']:
                SocialMediaAccount.objects.create(
                    influencer=influencer,
                    social_network=account_data['social_network'],
                    title=account_data['title'],
                    account_url=account_data['account_url'],
                    username=account_data['username'],
                    followers=account_data['followers']
                )
                self.stdout.write(self.style.SUCCESS(f'Created social media account: {account_data["title"]}'))

        self.stdout.write(self.style.SUCCESS('Data import complete.'))
