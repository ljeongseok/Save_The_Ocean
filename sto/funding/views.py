from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from funding.models import Funding, FundingInfo
from datetime import datetime
from django.urls import reverse_lazy
# Create your views here.

class FundingTemplateView(TemplateView):
    model = FundingInfo
    template_name="funding/funding_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fi = FundingInfo.objects.get(pk=3)
        context["object"] = fi
        context["remaining"] = fi.end_date - datetime.now()  # timedelta

        fundings = Funding.objects.filter(funding_info=fi)
        total = 0
        count=0
        for f in fundings:
            total += f.cash
            count += 1
    
        context["total"] = total
        context["rate"] = int(total / fi.goal_price * 100)
        context["count"] = count
        return context

class FundingListView(ListView):
    model = Funding
    template_name = 'funding/funding_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fi = FundingInfo.objects.get(pk=3)
        context["object"] = fi
        context["remaining"] = fi.end_date - datetime.now()  # timedelta

        fundings = Funding.objects.filter(funding_info=fi)
        total = 0
        count=0
        for f in fundings:
            total += f.cash
            count += 1
    
        context["total"] = total
        context["rate"] = int(total / fi.goal_price * 100)
        context["count"] = count
        return context

class FundingDetailView(DetailView):
    model = Funding


class FundingCreateView(CreateView):
    model = Funding
    fields = ['cash','funding_info']
    success_url = reverse_lazy('funding:index')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)



   
# def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         funding = context["object"]

#         context["remaining"] = funding.end_date - datetime.now()  # timedelta
#         print(context["remaining"])
#         return context