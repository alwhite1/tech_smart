from django.db import models

class E2E(models.Model):
    class Meta():
        db_table = 'E2E'

    CRASH_CODE = models.CharField(max_length=32)
    NODE_CODE = models.CharField(max_length=32)
    DISTRICT = models.CharField(max_length=32)
    S_ATV = models.IntegerField()
    S_VPTV = models.IntegerField()
    S_VBB = models.IntegerField()
    S_VBB_ETH = models.IntegerField()
    DATE_REPORT = models.CharField(max_length=32)
    DATE_BEGIN = models.CharField(max_length=32)
    DATE_OVER = models.CharField(max_length=32)
    CINTERVAL = models.CharField(max_length=32)
    CRASH_REASON = models.CharField(max_length=128)
    CRASH_DESCR = models.CharField(max_length=512)
    #CITY = models.CharField(max_length=16)
    HOUSE = models.CharField(max_length=32)
    HOUSE_ID = models.CharField(max_length=16)
    SYSUSER = models.CharField(max_length=16)
    Q_ABON_SERV_ATV = models.CharField(max_length=16)
    Q_ABON_SERV_DTV = models.IntegerField()
    Q_ABON_SERV_VBB = models.IntegerField()
    Q_ABON_SERV_ETH = models.IntegerField()
    Q_ABON_SERV_OTT = models.IntegerField()
    Q_ABON = models.IntegerField()
    COUNT_FLAT = models.IntegerField()
    TREATMENTS = models.IntegerField()
    DEPARTMENT = models.CharField(max_length=16)
    DATE_REG = models.CharField(max_length=16)
    DATE_OVEROPER = models.CharField(max_length=16)
    MONTH = models.CharField(max_length=8)

    def __unicode__(self):
        return self.id


class ReportCreator(models.Manager):
    def create_report(self, crash_code, date, data_begin, data_over, crash_interval,
                      time_in_business, time_not_in_business, crash_reason,
                      crash_description, number_of_affective, effect, effect_in_business,
                      effect_not_in_business, month):
        report = self.create(CRASH_CODE=crash_code, DATE=date, DATE_BEGIN=data_begin,
                             DATA_OVER=data_over, CRASH_INTERVAL=crash_interval, TIME_IN_BUSINESS=time_in_business,
                             TIME_NOT_IN_BUSINESS=time_not_in_business, CRASH_REASON=crash_reason,
                             CRASH_DESCRIPTION=crash_description, NUMBER_OF_AFFECTIVE=number_of_affective,
                             EFFECT=effect, EFFECT_IN_BUSINESS=effect_in_business,
                             EFFECT_NOT_IN_BUSINESS=effect_not_in_business, MONTH=month)
        return report
class SummaryCreator(models.Manager):
    def create_report(self, month_year, month, year, quarter, effect, effect_in_business, effect_not_in_business, quantity_of_crash):
        report = self.create(MONTH_YEAR=month_year, MONTH=month, YEAR=year, QUARTER=quarter, EFFECT=effect,
                             EFFECT_IN_BUSINESS=effect_in_business,
                             EFFECT_NOT_IN_BUSINESS=effect_not_in_business, QUANTITY=quantity_of_crash)
        return report

class CrashReport(models.Model):

    class Meta():
        db_table = 'CrashReport'

    def __unicode__(self):
        return self.CRASH_CODE

    CRASH_CODE = models.CharField(max_length=32)
    DATE = models.CharField(max_length=32)
    DATE_BEGIN = models.CharField(max_length=32)
    DATA_OVER = models.CharField(max_length=32)
    CRASH_INTERVAL = models.IntegerField()
    TIME_IN_BUSINESS = models.IntegerField(default=0)
    TIME_NOT_IN_BUSINESS = models.IntegerField(default=0)
    CRASH_REASON = models.CharField(max_length=128)
    CRASH_DESCRIPTION = models.CharField(max_length=512)
    NUMBER_OF_AFFECTIVE = models.IntegerField()
    EFFECT = models.FloatField(default=0)
    EFFECT_IN_BUSINESS = models.FloatField(default=0)
    EFFECT_NOT_IN_BUSINESS = models.FloatField(default=0)
    MONTH = models.CharField(max_length=8)

    objects = ReportCreator()

class MonthSummary(models.Model):

    class Meta():
        db_table = 'MonthSummary'

    MONTH_YEAR = models.CharField(max_length=9,default="4.2015")
    MONTH = models.IntegerField(default=0)
    YEAR = models.IntegerField(default=2015)
    QUARTER = models.IntegerField(default=0)
    EFFECT = models.FloatField(default=0)
    EFFECT_IN_BUSINESS = models.FloatField(default=0)
    EFFECT_NOT_IN_BUSINESS = models.FloatField(default=0)
    QUANTITY = models.IntegerField()

    def __unicode__(self):
        return self.MONTH

    objects = SummaryCreator()



class ReportInformation(models.Model):
    class Meta():
        db_table = 'ReportInformation'

    MONTH = models.CharField(max_length=9)
    TOTAL_RGU = models.IntegerField()
    TOTAL_TIME = models.IntegerField()
    TIME_IN_BUSINESS = models.IntegerField(default=0)
    TIME_NOT_IN_BUSINESS = models.IntegerField(default=0)
    STATUS = models.BooleanField()

    def __unicode__(self):
        return self.MONTH
