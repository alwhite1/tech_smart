from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tech_smart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tech_smart.views.main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', 'tech_smart.views.main'),
    url(r'^to/', include('to.urls')),
    url(r'^stp/', include('stp.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),


)
urlpatterns += staticfiles_urlpatterns()


