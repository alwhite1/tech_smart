#!/usr/bin/env python
# -*- coding: utf-8 -*-
import netsnmp
host = '77.121.96.226'
community_ro = 'public'
lv = netsnmp.Varbind('.1.3.6.1.4.1.35128.1.2.1.0')
get_lv = netsnmp.snmpget(lv, Version=1, DestHost=host, Community=community_ro)
print get_lv[0]