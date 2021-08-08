from django.shortcuts import render
from django.utils.translation import templatize
from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from donation.models import Donation
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # context['object']
        # 총 후원금을 계산
        total = 0
        rows = Donation.objects.filter(user=self.request.user)
        for i in rows:
            total += i.amount
        context['total'] = total
        return context

class NewsLetterView(TemplateView):
    template_name = 'donation/newsletter.html'

class IntroView(TemplateView):
    template_name = 'donation/intro.html'

class CampaignView(TemplateView):
    template_name = 'donation/campaign.html'