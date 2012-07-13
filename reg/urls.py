from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'reg.views.home'),
    url(r'^posts/$', 'reg.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'reg.views.post_detail'),
    ## add your url here
    url(r'^posts/search/(\w.*)', 'reg.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit', 'reg.views.edit_comment'),
)
