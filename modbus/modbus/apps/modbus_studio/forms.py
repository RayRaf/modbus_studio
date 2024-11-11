from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    unit = forms.CharField(
        label='Единица измерения', 
        required=False, 
        widget=forms.TextInput(attrs={'style': 'display: none;'})
    )

    class Meta:
        model = Device
        fields = ['tag', 'name', 'param_type', 'unit']
        labels = {
            'tag': 'Тэг',
            'name': 'Название параметра',
            'param_type': 'Тип параметра',
            'unit': 'Единица измерения',
        }
