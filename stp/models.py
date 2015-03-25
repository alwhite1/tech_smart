from django.db import models


class RealIp(models.Model):
    class Meta():
        db_table = 'RealIP'

    realip_ip = models.CharField(max_length=16)
    realip_mac = models.CharField(max_length=16)
    realip_cmts = models.CharField(max_length=11)
    realip_lou = models.CharField(max_length=3)
    realip_contract = models.CharField(max_length=30)
    realip_adress = models.CharField(max_length=255)

    def __unicode__(self):
        return self.realip_ip


class Wiki(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    content = models.TextField(max_length=10000, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id