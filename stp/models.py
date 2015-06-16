from django.db import models
from tinymce import models as tinymce_model

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
    class Meta():
        db_table = 'stp_wiki'

    name = models.CharField(max_length=255, primary_key=True)
    content = tinymce_model.HTMLField(max_length=10000, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

