from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^main/', 'to.views.main'),
                       url(r'^us_switch/', 'to.views.us_switch'),
                       url(r'^us_switch_vishenka/', 'to.views.vishenka'),
                       url(r'^us_switch_centr/', 'to.views.centr'),
                       url(r'^us_switch_zamostie/', 'to.views.zamostie'),
                       url(r'^switch/$', 'to.views.switch'),
                       url(r'^ppr/', 'to.views.ppr'),
                       url(r'^icsat/', 'to.views.e2e'),
                                              )
urlpatterns += staticfiles_urlpatterns()
