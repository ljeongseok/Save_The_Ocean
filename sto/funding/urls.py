from django.urls import path
from funding.views import *

app_name = 'funding'

urlpatterns = [
    path('',FundingTemplateView.as_view(),name ='index'),
    path('list/',FundingListView.as_view(),name ='funding'),
    path('<int:pk>/',FundingDetailView.as_view(),name ='funding_detail'),
]