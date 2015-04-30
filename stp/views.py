from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from stp.models import RealIp
from django.template import RequestContext
from stp.models import Wiki
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import markdown

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
        return render_to_response("stp_wiki_create.html", {"page_name": page_name})
    content = page.content
    return render_to_response("stp_wiki_view.html", {"page_name": page_name, "content": content})

@login_required
@csrf_exempt
def save_page(request, page_name):
    content = request.POST["content"]
    try:
        page = Wiki.objects.get(pk=page_name)
        page.content = content
    except Wiki.DoesNotExist:
        page = Wiki(name=page_name, content=content)
    page.save()
    return HttpResponseRedirect("/stp/wiki/" + page_name + "/")

@login_required
def edit_page(request, page_name):
    try:
        page = Wiki.objects.get(pk=page_name)
        content = page.content
    except Wiki.DoesNotExist:
        content = ""
    return render_to_response("stp_wiki_edit.html", {"page_name": page_name,"content": content})