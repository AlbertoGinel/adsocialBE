from django.urls import path
from . import views

urlpatterns = [
    path('influencers/', views.influencers_list, name='influencers_list'),
    path('influencers/<int:pk>/', views.influencer_detail, name='influencer_detail'),
    path('influencers/filtered/', views.influencers_list_filtered, name='influencers_list_filtered'),
    path('social-media-accounts/', views.social_media_account_list, name='social_media_account_list'),
    path('social-media-accounts/<int:pk>/', views.social_media_account_detail, name='social_media_account_detail'),
    path('managers/', views.manager_list, name='manager_list'),
    path('managers/<int:pk>/', views.manager_detail, name='manager_detail'),
]
