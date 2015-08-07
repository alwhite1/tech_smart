# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from e2e.models import E2E
from e2e.models import CrashReport
from e2e.models import ReportInformation
from e2e.e2e import change_time
from e2e.e2e import time_period
from django.template import RequestContext
import datetime

@login_required
def main(request):
    return render_to_response('e2e_main_data.html',
                              context_instance=RequestContext(request))
@login_required
def report(request):
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    dict_month = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
                  9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    year_list = []
    status1 =[]

    state_all = []
    report = ReportInformation.objects.all()
    for year in range(2015, current_year + 1):
        year_list.append(year)
    for key, val in dict_month.items():
        state_month = []
        state_month.append(val)
        for year in year_list:
            date = str(key) + "." + str(year)
            status = report.filter(MONTH=date).values('STATUS')
            status1.append(status)
            state = "Создание отчета невозможно"
            if status:
                state = "Очет создан"
            if not status:
                state = " Отчет еще не создан "
            state_month.append(state)
        state_all.append(state_month)
    return render_to_response('e2e_report.html', {'state_all': state_all, "year_list": year_list, 'status1': status1
                                                  })


@login_required
def generate_month_report(request, month):
    additional = ReportInformation.objects.filter(MONTH=month)
    rgu_all = 0
    e2e_all = 100
    if not additional.STATUS:
        crash_array = []
        crash_all = E2E.objects.all()
        for crash in crash_all:
            if crash.CRASH_CODE not in crash_array:
                crash_array.append(crash.CRASH_CODE)
        crash_number = len(crash_array) - 1
        for crash in crash_array:
            crash_summary = E2E.objects.filter(CRASH_CODE=crash)
            rgu = 0
            for single_record in crash_summary:
                if int(single_record.S_ATV) != 0:
                    rgu += int(single_record.Q_ABON_SERV_ATV)
                if int(single_record.S_VPTV) != 0:
                    rgu += int(Q_ABON_SERV_AT)
                if int(single_record.S_VBB) != 0:
                    rgu += int(Q_ABON_SERV_VBB)
                first_record = crash_summary.objects.filter()[:1].get()
                crash_description = first_record.CRASH_DESCR
                date = first_record.DATE_REPORT.split(" ")[0]
                data_begin = first_record.DATE_BEGIN
                date_over = first_record.DATE_OVER
                time = time_period(data_begin,date_over)
                time_in_business = time[0]
                time_not_in_business = time[1]
                crash_interval = change_time(first_record.CINTERVAL)
                crash_reason = first_record.CRASH_REASON
                number_of_affective = rgu
                effect = float(crash_interval) * float(rgu) * 100 / (float(additional.TOTAL_RGU) *
                                                                     float(additional.TOTAL_TIME))
                effect_in_business = float(time_in_business) * float(rgu) * 100 / (float(additional.TOTAL_RGU) * float(additional.TIME_IN_BUSINESS))
                effect_not_in_business = float(time_not_in_business) * float(rgu) * 100 / (float(additional.TOTAL_RGU) * float(additional.TIME_NOT_IN_BUSINESS))
                report = CrashReport.objects.create_report(crash, date, data_begin, date_over, crash_interval,
                                                           time_in_business, time_not_in_business, crash_reason,
                                                           crash_description, number_of_affective, effect,
                                                           effect_in_business, effect_not_in_business, month)
                rgu_all += rgu
                e2e_all -= effect
        additional.STATUS = True
        additional.save()

        return render_to_response('e2e_generate_month_report.html', {'month': month, 'crash_number': crash_number,
                                                                     'affective_number': rgu_all, 'e2e': e2e_all},
                                  context_instance=RequestContext(request))