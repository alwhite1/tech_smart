from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from stp.models import RealIp
from django.template import RequestContext


@login_required
def main(request):
    return render_to_response('stp_main.html',
                              context_instance=RequestContext(request))

@login_required
def index(request):
    return render_to_response('stp_realip_all.html',
                              context_instance=RequestContext(request))
@login_required
def realipmain(request):

    return render_to_response('stp_realip_main.html',
                              context_instance=RequestContext(request))

@login_required
def realip(request):
    ip_base = RealIp.objects.all()
    return render_to_response('stp_realip_all.html', {'ip_base': ip_base},
                              context_instance=RequestContext(request))

@login_required
def realipcmts(request, cmts):
    ip_base = RealIp.objects.filter(realip_cmts=cmts)
    return render_to_response('stp_realip_cmts.html', {'ip_base': ip_base, 'cmts': cmts},
                              context_instance=RequestContext(request))

@login_required
def subnet(request):
    return render_to_response('stp_subnet.html',
                              context_instance=RequestContext(request))


