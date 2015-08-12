# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from to.models import Staffer

@login_required
def main(request):
    staff = Staffer.objects.filter(staffer_position='Главный инженер')
    return render_to_response('main_data.html', {'staff': staff},
                              context_instance=RequestContext(request))
