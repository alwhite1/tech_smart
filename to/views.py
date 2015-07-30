# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from to.form import LOUFormsCen, LOUFormsVish, LOUFormsZam
from to.models import LOU
from django.template import RequestContext
from to.switching import Switching
from django.contrib.auth.decorators import login_required
from to.models import Staffer

@login_required
def main(request):
    staff_sto = Staffer.objects.filter(staffer_department='Служба технического обслуживания')
    staff_stpi = Staffer.objects.filter(staffer_department='Служба технической поддержки интернет')
    staff_pts = Staffer.objects.filter(staffer_department='Производствено-техническая служба')
    staff_stovols = Staffer.objects.filter(staffer_department='Служба технического обслуживания ВОЛС')
    return render_to_response('to_main_data.html', {'staff_sto': staff_sto, 'staff_stpi': staff_stpi,
                                                    'staff_pts': staff_pts, 'staff_stovols': staff_stovols},
                              context_instance=RequestContext(request))

def us_switch(request):
    return render_to_response('to_us_switch_main.html',
                              context_instance=RequestContext(request))

@login_required
def vishenka(request):
    return render_to_response('to_switch_vishenka.html',
                              {'form': LOUFormsVish},
                              context_instance=RequestContext(request))

@login_required
def centr(request):
    return render_to_response('to_us_switch_centr.html',
                              {'form': LOUFormsCen},
                              context_instance=RequestContext(request))

@login_required
def zamostie(request):
    return render_to_response('to_us_switch_zamostie.html',
                              {'form': LOUFormsZam},
                              context_instance=RequestContext(request))

@login_required
def change_fr(request):
    return render_to_response('to_change_fr.html',
                              context_instance=RequestContext(request))

@login_required
def view_level(request):
    return render_to_response('to_get_power_level.html',
                              context_instance=RequestContext(request))


@login_required
def switch(request, lou_name='lou_name'):
    lou_i = request.POST[lou_name]
    swit = LOU.objects.get(id=lou_i)
    sw = swit.lou_switch
    port = swit.lou_port
    name = swit.lou_name
    switc = Switching()
    result = switc.switch(sw, port)
    return render_to_response('to_switch.html', {'switch': sw, 'port': port, 'name': name,
                                                 'result': result},
                              context_instance=RequestContext(request))

@login_required
def ppr(request):
    return render_to_response('to_ppr.html',
                              context_instance=RequestContext(request))

@login_required
def e2e(request):
    return render_to_response('to_e2e.html',
                              context_instance=RequestContext(request))
