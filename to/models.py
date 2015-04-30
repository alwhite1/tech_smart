from django.db import models
from tinymce import models as tinymce_model


class LOU(models.Model):
    class Meta():
        db_table = 'LOU'

    lou_name = models.CharField(max_length=32)
    lou_switch = models.CharField(max_length=16)
    lou_port = models.CharField(max_length=11)

    def __unicode__(self):
        return self.lou_name

    def get_sw_port(self, name):
        switch = LOU(lou_id=name)
        sw = switch.lou_switch
        port = switch.lou_port
        return sw, port

class Staffer(models.Model):
    class Meta():
        db_table = 'Staffer'

    staffer_name = tinymce_model.HTMLField(max_length=64)
    staffer_position = tinymce_model.HTMLField(max_length=64)
    staffer_email = tinymce_model.HTMLField(max_length=32)
    staffer_phone = tinymce_model.HTMLField(max_length=32)

    def __unicode__(self):
        return self.staffer_name

