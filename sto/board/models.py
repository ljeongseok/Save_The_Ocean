from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, 
    help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,
        verbose_name='USER', blank=True, null=True)

    hits = models.PositiveIntegerField("조회수",default=0)

    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'board_posts'
        ordering = ('-create_dt',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:detail', args=(self.id,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self,*args,**kwargs):
        #필드 조정 필요시 작성
        super().save(*args,**kwargs)

    @property
    def hits_count(self):
        self.hits = self.hits + 1
        self.save()

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True,
        related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer= models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.comment_contents