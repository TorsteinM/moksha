from django.conf.urls import url

from . import views

app_name = 'Moksha'


urlpatterns = [

    url(r'^PersonDelete/(?P<pk>[0-9]+)/$', views.PersonDelete.as_view(), name='person_delete'),
    url(r'^PersonUpdate/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view(), name='person_update'),
    url(r'^DeleteEvent/(?P<pk>[0-9]+)/$', views.DeleteEvent.as_view(), name='event_delete'),
    url(r'^UpdateEvent/(?P<pk>[0-9]+)/$', views.UpdateEvent.as_view(), name='event_update'),
    url(r'^PersonCreate/$', views.PersonCreate.as_view(), name='person_create'),
    url(r'^CreateEvent/$', views.CreateEvent.as_view(), name='create_event'),
    url(r'^personnel/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(), name='person_detail'),
    url(r'^personnel/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='event_detail'),
    url(r'^events/$', views.EventListView.as_view(), name='event_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^$', views.IndexView.as_view(), name='home'),

]
