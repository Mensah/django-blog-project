from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'blogg.views.home'),
    url(r'^posts/$', 'blogg.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blogg.views.post_detail'),
    ## add your url here
    url(r'^posts/search/(\w.*)', 'blogg.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit', 'blogg.views.edit_comment'),
)
