from board.views import *
from django.contrib import admin
from django.urls import path


app_name = 'board'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/',PostListView.as_view(),name='list'),
    path('<int:pk>/',PostDetailView.as_view(), name="detail"),
    path('add/', PostCreateView.as_view(), name="add"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),
    path('<int:pk>/comment/', comment_create,name="comment"),
    path('comment_delete/<int:pk>', CommentDeleteView.as_view(),name="comment_delete"),
    path('<int:pk>/like/',likes,name="like"),
]
