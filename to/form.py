# ~*~ coding: utf-8 ~*~
__author__ = 'abelyaev'
from django import forms
from to.models import LOU


class LOUFormsZam(forms.ModelForm):
    class Meta():
        model = LOU
        fields = ['lou_name', ]
    zamos_switch = ['4', '5', '8']
    lou_name = forms.ModelChoiceField(queryset=LOU.objects.filter(lou_switch__in=zamos_switch).order_by('lou_name'),
                                      empty_label=" ",
                                      widget=forms.Select(attrs={'class': 'dropdown', 'label': 'LOU'}),
                                      label='ЛОУ Замостье:')

class LOUFormsCen(forms.ModelForm):
    class Meta():
        model = LOU
        fields = ['lou_name', ]
    cent_switch = ['1', '2', '3']
    lou_name = forms.ModelChoiceField(queryset=LOU.objects.filter(lou_switch__in=cent_switch).order_by('lou_name'),
                                      empty_label=" ",
                                      widget=forms.Select(attrs={'class': 'dropdown', }),
                                      label='ЛОУ Центр:')

class LOUFormsVish(forms.ModelForm):
    class Meta():
        model = LOU
        fields = ['lou_name', ]
    vishen_switch = ['6', '7']
    lou_name = forms.ModelChoiceField(queryset=LOU.objects.filter(lou_switch__in=vishen_switch).order_by('lou_name'),
                                      empty_label=" ",
                                      widget=forms.Select(attrs={'class': 'dropdown', }),
                                      label='ЛОУ Вишенка:')
