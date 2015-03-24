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
                       url(r'^change_fr/', 'to.views.change_fr'),
                       url(r'^view_level/', 'to.views.view_level'),
                       url(r'^get_power_level/', 'to.views.get_power_level'),
                       )
urlpatterns += staticfiles_urlpatterns()
