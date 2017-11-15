from django import forms
from Moksha.models import Event, Person


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_start', 'attendants', ]


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']
