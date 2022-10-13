from django import forms
from .models import *


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = (
            'name',
        )


class CreateChapelForm(forms.ModelForm):
    class Meta:
        model = Chapels
        fields = (
            'name',
        )


class CreateMemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = (
            'first_name', 'last_name', 'other_name', 'title',
            'sex', 'chapel', 'group', 'dob', 'phone_number', 'whatsapp_number',
            'other_phone_number', 'area_of_residence', 'gps_address',
        )