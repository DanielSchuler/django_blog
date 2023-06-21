# DJANGO IMPORTS

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# DJANGO IMPORTS FOR CANONICAL URL
from django.urls import reverse
# DJANGO THIRD PARTY IMPORTS
from taggit.managers import TaggableManager

#Create custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# Create your models here.
'''
Now, you can import the Post model and retrieve all published posts whose title
starts with Who, executing the following QuerySet:
>>> from blog.models import Post
>>> Post.published.filter(title__startswith='Who')
To obtain results for this QuerySet, make sure that you set the published field to
True in the Post object whose title starts with Who.
'''
class Post(models.Model):
    tags = TaggableManager()
    object=models.Manager()#Default Manager
    published=PublishedManager() #Our custom manager
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    #CANONICAL URL
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
