
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^main/', 'e2e.views.main'),
                       url(r'^report/', 'e2e.views.report'),
                       url(r'^generate_month_report/', 'e2e.views.generate_month_report'),
                       url(r'^see_post/', 'e2e.views.see_post'),
                       url(r'^month_report/', 'e2e.views.month_report'),
                       url(r'^json_report/(?P<month_year>[0-9]+[\.]+[20]+[1-2]+[1-9])', 'e2e.views.month_json'),
                       url(r'(?P<month_year>[0-9]+[\.]+[20]+[1-2]+[1-9])', 'e2e.views.month_detailed'),
                       )

urlpatterns += staticfiles_urlpatterns()
