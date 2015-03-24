from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render_to_response('main_new_1.html',
                              context_instance=RequestContext(request))

@login_required
def to(request):
    return render_to_response('to.html',
                              context_instance=RequestContext(request))

@login_required
def stp(request):
    return render_to_response('stp_main.html',
                              context_instance=RequestContext(request))




# Create your views here.
