from django.shortcuts import render
from django.utils.translation import templatize
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from donation.models import Donation
from django.urls import reverse_lazy
# Create your views here.

class PersonListView(TemplateView):
    template_name = 'donation/donation_amount.html'

# CreateView
class DonationCreateView(CreateView):
    model = Donation
    fields = ['amount','card','card_num']
    # success_url = reverse_lazy('donation:donation_fin')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        # print(self.request.user, self.request.user.id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('donation:donation_fin', args=(self.object.id, ))

class FinalDetailView(DetailView):
    model = Donation
    template_name = 'donation/End.html'

class NewsLetterView(TemplateView):
    template_name = 'donation/newsletter.html'

class IntroView(TemplateView):
    template_name = 'donation/intro.html'

class CampaignView(TemplateView):
    template_name = 'donation/campaign.html'