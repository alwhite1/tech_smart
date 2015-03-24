# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from to.form import LOUFormsCen,LOUFormsVish,LOUFormsZam
from to.models import LOU
from django.template import RequestContext
from to.switching import SwithToUs, SwichToPort, Switching
from django.contrib.auth.decorators import login_required
import os
import netsnmp
import time

@login_required
def main(request):
    return render_to_response('to_main.html',
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
    kws = ''
    name = swit.lou_name
    switc = Switching()
    result = switc.switch(sw, port)
    #community_rw = 'private'
    #community_ro = 'public'
    #host = '77.121.96.226'
    #frenq = '36'
    #on_kws = os.popen("snmpset -v 1 -c " + community_rw + " " + host + " .1.3.6.1.4.1.35128.1.1.3.0 s RC")
    #time.sleep(5)
    #fr_set = os.popen("snmpset -v 1 -c " + community_rw + " " + host + " .1.3.6.1.4.1.35128.1.1.6.0 s " + frenq)
    #fr = netsnmp.Varbind('.1.3.6.1.4.1.35128.1.1.6.0')
    #rc = netsnmp.Varbind('.1.3.6.1.4.1.35128.1.1.3.0')
    #time.sleep(5)
   # get_fr = netsnmp.snmpget(fr, Version=1, DestHost=host, Community=community_ro)
   # time.sleep(5)
    #get_rc = netsnmp.snmpget(rc, Version=1, DestHost=host, Community=community_ro)
   # if get_rc[0] == 'RC':
    #    kws = "Включен"
   # else:
   #     kws = "Включен"

    return render_to_response('to_switch.html', {'switch': sw, 'port': port, 'name': name,
                                                 'result': result},
                              context_instance=RequestContext(request))

@login_required
def ppr(request):
    return render_to_response('to_ppr.html',
                              context_instance=RequestContext(request))

@login_required
def get_power_level(request):
    lv = netsnmp.Varbind('.1.3.6.1.4.1.35128.1.2.1.0')
    host = '77.121.96.226'
    community_ro = 'public'
    get_lv = netsnmp.snmpget(lv, Version=1, DestHost=host, Community=community_ro)
    return render_to_response('to_get_power_level_1.html',{'get_lv': get_lv[0]},
                              context_instance=RequestContext(request))