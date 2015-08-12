# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from stp.models import RealIp
from django.template import RequestContext
from stp.models import Wiki
from to.models import Staffer

@login_required
def main(request):
    staff = Staffer.objects.filter(staffer_department='Служба поддержки сети')
    return render_to_response('stp_main_data.html', {'staff': staff},
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

@login_required
def wiki(request):
    return render_to_response('stp_wiki.html',
                              context_instance=RequestContext(request))

@login_required
def wiki(request):
    pages = Wiki.objects.all()
    return render_to_response('stp_wiki.html', {'pages': pages},
                              context_instance=RequestContext(request))
@login_required
def view_page(request, page_name):
    try:
        page = Wiki.objects.get(pk=page_name)
    except Wiki.DoesNotExist:
        return render_to_response("stp_wiki_DoesNotExist.html", {"page_name": page_name})
    content = page.content
    return render_to_response("stp_wiki_view.html", {"page_name": page_name, "content": content})

