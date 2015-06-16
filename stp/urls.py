__author__ = 'abelyaev'
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^main/', 'stp.views.main'),
                       url(r'^realip/$', 'stp.views.realipmain'),
                       url(r'^realip/(?P<cmts>(sub-vn-)+[0-3]+[\-]+[1-6])', 'stp.views.realipcmts'),
                       url(r'^realip/all/', 'stp.views.realip'),
                       url(r'^subnet/', 'stp.views.subnet'),
                       url(r'^wiki/$', 'stp.views.wiki'),
                       url(r'^wiki/(?P<page_name>[^/]+)/$', 'stp.views.view_page'),
                       )
urlpatterns += staticfiles_urlpatterns()
