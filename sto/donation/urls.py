from django.urls import path
from donation.views import *

app_name = 'donation'

urlpatterns = [
    path('',PersonListView.as_view(),name ='index'),
    path('donationC/',DonationCreateView.as_view(), name= 'donation_check'),
    path('donationF/<int:pk>',FinalDetailView.as_view(), name='donation_fin'),
    path('newsletter/',NewsLetterView.as_view(),name ='newsletter'),
    path('intro/',IntroView.as_view(),name='intro'),
    path('campaign/',CampaignView.as_view(),name='campaign'),
]