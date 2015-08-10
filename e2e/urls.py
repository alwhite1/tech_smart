
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^main/', 'e2e.views.main'),
                       url(r'^report/', 'e2e.views.report'),
                       )

urlpatterns += staticfiles_urlpatterns()