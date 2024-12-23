from rest_framework import serializers
from .models import Influencer, SocialMediaAccount, Manager

class SocialMediaAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaAccount
        fields = ['id', 'social_network', 'title', 'account_url', 'followers', 'influencer', 'username']

class InfluencerSerializer(serializers.ModelSerializer):
    social_media_accounts = SocialMediaAccountSerializer(many=True, read_only=True)
    manager_name = serializers.SerializerMethodField()
    manager = serializers.PrimaryKeyRelatedField(
        queryset=Manager.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Influencer
        fields = ['id', 'first_name', 'last_name', 'social_media_accounts', 'manager', 'manager_name']

    def get_manager_name(self, obj):
        if obj.manager:
            return f"{obj.manager.first_name} {obj.manager.last_name}"
        return None  # Return None if no manager is assigned


class ManagerSerializer(serializers.ModelSerializer):
    influencers = InfluencerSerializer(many=True, read_only=True)

    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'influencers']
