from django.contrib import admin
from .models import Influencer, SocialMediaAccount, Manager

class SocialMediaAccountInline(admin.TabularInline):
    model = SocialMediaAccount
    extra = 1
    fields = ('social_network', 'title', 'username','account_url', 'followers')

@admin.register(Influencer)
class InfluencerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'manager')
    search_fields = ('first_name', 'last_name', 'manager__first_name', 'manager__last_name')
    list_filter = ('manager',)
    ordering = ('manager', 'last_name', 'first_name')
    inlines = [SocialMediaAccountInline]
    fields = ('first_name', 'last_name', 'manager')

# Register the Manager model
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')

    # Optional: Inline for related influencers
    class InfluencerInline(admin.TabularInline):  # You can also use StackedInline
        model = Influencer
        extra = 0
        fields = ('first_name', 'last_name')

    inlines = [InfluencerInline]
