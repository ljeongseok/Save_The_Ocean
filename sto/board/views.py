from django.db import models
from django.http.response import HttpResponseRedirect
from board.models import Post, Comment
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import OwnerOnlyMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator 

class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    context_object_name='posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        likes=[ post for post in Post.objects.all() if post.like.count() > 0 ]
        likes.sort(key=lambda p : p.like.count(), reverse=True)
        context['likes'] = likes[:5]
        
        return context


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

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('board:list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


def comment_create(request, pk):
    post_id = request.POST['post']
    content = request.POST['content']
    user = request.user

    post = Post.objects.get(pk=post_id)
    
    if content=='':
        return HttpResponseRedirect(reverse('board:detail', args=(post.id,)))
    else:
        comment = Comment(post=post, comment_contents = content, comment_writer=user)
        comment.save()
        # print('----- db 저장 ')
        # 리다이렉트 --> 
        return HttpResponseRedirect(reverse('board:detail', args=(post.id,)))

class CommentDeleteView(OwnerOnlyMixin, DeleteView):
    model = Comment
    # success_url  ---> 인자가 없는 경우 

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    # success_url을 동적으로 생성하는 경우 
    def get_success_url(self):
        postid = self.get_object().post.id

        return reverse_lazy('board:detail',args=(postid,))

# def comment_delete(request,pk):
#     comment= get_object_or_404(Post,id = pk)
#     post= get_object_or_404(Post,id = pk)
    
#     if request.method =='POST':
#         comment.delete()
#         return HttpResponseRedirect(reverse('board:detail', args=(post.id,)))


def likes(request,pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.like.all():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)

    return HttpResponseRedirect(reverse('board:detail', args=(post.id,)))




# class CommentCreateView(CreateView):
#     model = Comment
#     fields = ['post', 'content']

#     def form_valid(self):
#         print(self.form.instance)
#         pass
