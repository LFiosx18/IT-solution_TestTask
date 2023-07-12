from .models import Settings
from django.forms import ModelForm, TextInput


class SettingsFrom(ModelForm):
    class Meta:
        model = Settings
        fields = ["title", "color_text", "color_back", "fps", "time", "width", "height"]
        widgets = {
            "title": TextInput(attrs={
                'id': 'text',
                'type': 'text',
                'placeholder': 'Ваш текст'
            }),
            "color_text": TextInput(attrs={
                'id': 'color_text',
                'class': 'color',
                'type': 'color',
                'value': '#4A3DFF'
            }),
            "color_back": TextInput(attrs={
                'id': 'color_back',
                'class': 'color',
                'type': 'color',
                'value': '#DBDFFF'
            }),
            "fps": TextInput(attrs={
                'id': 'color_back',
                'type': 'range',
                'list': 'values_fps',
                'min': '20',
                'max': '100',
                'step': '20',
                'value': '60'
            }),
            "time": TextInput(attrs={
                'id': 'time',
                'class': 'el',
                'type': 'number',
                'min': '1',
                'max': '60',
                'value': '1'
            }),
            "width": TextInput(attrs={
                'id': 'width',
                'class': 'el',
                'type': 'number',
                'min': '50',
                'max': '500',
                'value': '100'
            }),
            "height": TextInput(attrs={
                'id': 'height',
                'class': 'el',
                'type': 'number',
                'min': '50',
                'max': '500',
                'value': '100'
            })
        }