# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from e2e.models import E2E
from e2e.models import CrashReport, MonthSummary
from e2e.models import ReportInformation
from e2e.e2e import change_time
from e2e.e2e import time_period
from  e2e.e2e import get_month_report
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
    status1 = []
    state_all = []
    state = ""
    month_report_all = ReportInformation.objects.all()
    for year in range(2015, current_year + 1):
        year_list.append(year)
    for key, val in dict_month.items():
        state_month = []
        state_month.append(str(val))
        for year in year_list:
            date = str(key) + "." + str(year)
            month_report = month_report_all.filter(MONTH=date)
            if month_report.exists():
                for crash_report in month_report:
                    status = crash_report.STATUS
                    status1.append(str(state))
                    if status:
                        state = "Очет создан"
                        status1.append(str(status))
                    if not status:
                        state = " Отчет еще не создан "
                        status1.append(str(state))
            else:
                state = "Создание отчета невозможно"
                status1.append(str(state))
            state_month.append(str(state))
        state_all.append(state_month)
    return render_to_response('e2e_report.html', {'state_all': state_all, "year_list": year_list,
                                                  'dict_month': dict_month},
                              context_instance=RequestContext(request))


def see_post(request):
    month = request.POST["month"]
    year = request.POST["year"]
    return render_to_response('see_post.html', {'month': month, 'year': year},
                              context_instance=RequestContext(request))
def test_filter_crash(request):
    MONTH = "6.2015"
    crash_array = []
    crash_all = E2E.objects.filter(MONTH=MONTH)
    for crash in crash_all:
        if crash.CRASH_CODE not in crash_array:
            crash_array.append(crash.CRASH_CODE)
    return render_to_response('see_post.html', {'crash_array': crash_array},
                              context_instance=RequestContext(request))




@login_required
def generate_month_report(request):
    month = request.POST["month"]
    year = request.POST["year"]
    month_year = str(month) + "." + str(year)
    additional = ReportInformation.objects.filter(MONTH=month_year)
    if month in (1, 2, 3):
        quater = 1
    elif month in(4, 5, 6):
        quater = 2
    elif month in (7, 8, 9):
        quater = 3
    else:
        quater = 4

    for record in additional:
        TOTAL_RGU = record.TOTAL_RGU
        TIME_IN_BUSINESS = record.TIME_IN_BUSINESS
        TIME_NOT_IN_BUSINESS = record.TIME_NOT_IN_BUSINESS
        TOTAL_TIME = record.TOTAL_TIME
        status = record.STATUS
    rgu_all = 0
    e2e_all = 100
    e2e_business = 100
    e2e_not_business = 100
    if not status:
        crash_array = []
        crash_all = E2E.objects.filter(MONTH=month_year)
        for crash in crash_all:
            if crash.CRASH_CODE not in crash_array:
                crash_array.append(crash.CRASH_CODE)
        crash_number = len(crash_array)
        for crash in crash_array:
            crash_summary = E2E.objects.filter(CRASH_CODE=crash)
            rgu = 0
            for single_record in crash_summary:
                if int(single_record.S_ATV) != 0:
                    rgu += int(single_record.Q_ABON_SERV_ATV)
                if int(single_record.S_VPTV) != 0:
                    rgu += int(single_record.Q_ABON_SERV_DTV)
                if int(single_record.S_VBB) != 0:
                    rgu += int(single_record.Q_ABON_SERV_VBB)
                first_record = crash_summary.filter()[:1].get()
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
                effect = float(crash_interval) * float(rgu) * 100 / (float(TOTAL_RGU) * float(TOTAL_TIME))
                effect_in_business = float(time_in_business) * float(rgu) * 100 / (float(TOTAL_RGU) * float(TIME_IN_BUSINESS))
                effect_not_in_business = float(time_not_in_business) * float(rgu) * 100 / (float(TOTAL_RGU) * float(TIME_NOT_IN_BUSINESS))
            crash_report = CrashReport.objects.create_report(crash, date, data_begin, date_over, crash_interval,
                                                           time_in_business, time_not_in_business, crash_reason,
                                                           crash_description, number_of_affective, effect,
                                                           effect_in_business, effect_not_in_business, month_year)

            rgu_all += rgu
            e2e_all -= effect
            e2e_business -= effect_in_business
            e2e_not_business -= effect_not_in_business
        month_summary = MonthSummary.objects.create_report(month_year, month, year, quater, e2e_all, e2e_business,
                                                           e2e_not_business, crash_number)
        record.STATUS = True
        record.save()

        return render_to_response('e2e_generate_month_report.html', {'month': month, 'crash_number': crash_number,
                                                                     'affective_number': rgu_all, 'e2e': e2e_all,
                                                                     'e2e_business': e2e_business,
                                                                     'e2e_not_business': e2e_not_business },
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('e2e_generate_error_month_report.html', {'month': month, 'year': year},
                                  context_instance=RequestContext(request))

def month_report(request):
    dict_month = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
                  9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    summary = MonthSummary.objects.all()
    return render_to_response('e2e_month_report.html', {'summary': summary, "dict_month": dict_month},
                              context_instance=RequestContext(request))

def month_detailed(request, month_year):
    dict_month = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
                  9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    month = month_year.split(".")[0]
    year = month_year.split(".")[1]
    crash_report = CrashReport.objects.filter(MONTH=month_year).order_by('-EFFECT_IN_BUSINESS')
    return render_to_response('e2e_month_detailed.html', {'crash_report': crash_report, "dict_month": dict_month,
                                                          "month": month, "year": year, "month_year":month_year},
                              context_instance=RequestContext(request))


