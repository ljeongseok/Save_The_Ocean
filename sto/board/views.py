from django.db import models
from django.http.response import HttpResponseRedirect
from board.models import Post, Comment
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import OwnerOnlyMixin
from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
from django.urls import reverse

class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    context_object_name='posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'content']
    success_url = reverse_lazy('board:list')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content']
    success_url = reverse_lazy('board:list')

class PostDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('board:list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)



def comment_create(request, pk):
    post_id = request.POST['post']
    content = request.POST['content']
    user = request.user

    post = Post.objects.get(pk=post_id)
    comment = Comment(post=post, comment_contents = content, comment_writer=user)
    comment.save()
    # print('----- db 저장 ')
    # 리다이렉트 --> 
    return HttpResponseRedirect(reverse('board:detail', args=(post.id,)))






# class CommentCreateView(CreateView):
#     model = Comment
#     fields = ['post', 'content']

#     def form_valid(self):
#         print(self.form.instance)
#         pass
