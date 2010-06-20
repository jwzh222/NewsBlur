from django.conf.urls.defaults import *
from apps.reader import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^logout', views.logout, name='logout'),
    url(r'^login', views.login, name='login'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^load_single_feed', views.load_single_feed),
    url(r'^load_feed_page', views.load_feed_page),
    url(r'^load_feeds_iphone', views.load_feeds_iphone, name='load-feeds-iphone'),
    url(r'^load_feeds', views.load_feeds, name='load-feeds'),
    url(r'^refresh_feeds', views.refresh_feeds, name='refresh-feeds'),
    url(r'^mark_all_as_read', views.mark_all_as_read, name='mark-all-as-read'),
    url(r'^mark_story_as_read', views.mark_story_as_read),
    url(r'^mark_story_as_like', views.mark_story_as_like),
    url(r'^mark_story_as_dislike', views.mark_story_as_dislike),
    url(r'^mark_feed_as_read', views.mark_feed_as_read),
    url(r'^delete_feed', views.delete_feed, name='delete-feed'),
    url(r'^add_url', views.add_url),
    url(r'^add_folder', views.add_folder),
    url(r'^add_feature', views.add_feature, name='add-feature'),
)
