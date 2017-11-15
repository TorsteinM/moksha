from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Person, Event
from .forms import EventForm, PersonForm


class IndexView(generic.ListView):
    template_name = "Moksha/index.html"
    context_object_name = 'upcoming_events'

    def get_queryset(self):
        return Event.objects.filter(event_start__gte=timezone.now()).order_by('-event_start')[:5]


def contact(request):
    return render(request, 'Moksha/contact.html')


def about(request):
    return render(request, 'Moksha/about.html')


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'Moksha/event_detail.html'


class EventListView(generic.ListView):
    model = Event

    # get context data(All Event objects) and add EventForm to the context
    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['event_form'] = EventForm()
        return context


class CreateEvent(generic.FormView):
    template_name = 'Moksha/event_create.html'
    model = Event
    form_class = EventForm
    fields = ['event_name', 'event_start', 'attendants']
    success_url = reverse_lazy('Moksha:event_list')

    def form_valid(self, form):
        my_form = EventForm(self.request.POST)
        my_form.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateEvent(generic.UpdateView):
    template_name = 'Moksha/event_update.html'
    model = Event
    form_class = EventForm


class DeleteEvent(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('Moksha:event_list')


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'Moksha/person_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        return context


class PersonDelete(generic.DeleteView):
    model = Person
    success_url = reverse_lazy('Moksha:person_list')


class PersonUpdate(generic.UpdateView):
    template_name = 'Moksha/person_update.html'
    model = Person
    form_class = PersonForm


class PersonCreate(generic.CreateView):
    template_name = 'Moksha/person_create.html'
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('Moksha:person_list')


class PersonListView(generic.ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['form'] = PersonForm()
        return context
