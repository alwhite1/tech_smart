from tastypie.resources import ModelResource
from e2e.models import CrashReport

class CrashReportResource(ModelResource):
    class Meta:
        limit = 0
        queryset = CrashReport.objects.all()
        resource_name = 'report'
