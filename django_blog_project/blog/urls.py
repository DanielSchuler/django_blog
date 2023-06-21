#DJANGO IMPORTS
from django.urls import path
# FEEDS IMPORTS
from .feeds import LatestPostsFeed
#IMPORT FUNCTION VIEWS
from .views import post_list, post_detail,post_share,post_search
#IMPORT CLASS VIEW
from .views import PostListView
app_name = 'blog'
urlpatterns = [
# post views
path('', post_list, name='post_list'),
path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
#path('', PostListView.as_view(), name='post_list'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
path('<int:post_id>/share/',post_share, name='post_share'),
path('feed/', LatestPostsFeed(), name='post_feed'),
path('search/', post_search, name='post_search'),
]
