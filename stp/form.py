__author__ = 'abelyaev'
from django import forms
from stp.models import RealIp

class TableIp(forms.ModelForm):
    class Meta():
        model = RealIp
        fields = ['realip_ip', 'realip_mac', 'realip_cmts', 'realip_lou', 'realip_contract', 'realip_adress']

    ip - forms.CharField()
    mac - forms.CharField()

