from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied

# Create your views here.

class UserCreateView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm  

    # success_url = 회원가입 성공시 리다이렉트링크
    success_url = reverse_lazy('accounts:register_done')
    
    
class UserCreateDoneView(generic.TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception= True
    permission_denied_message = "owner only can update/delete the object"

    # get 요청시에 동작 
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()     # 모델 인스턴스 얻기
        
        # self.request.user : 로그인 사용자 // self.object. : 북마크
        if self.request.user != self.object.user:
            self.handle_no_permission()
        
        return super().get(request,*args,**kwargs)

# 로그인 성공 리디이렉트
# return redirect(self.request.GET.get('next'))
