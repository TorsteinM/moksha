from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=30)
    attendants = models.ManyToManyField('Person')
    event_start = models.DateTimeField()

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('Moksha:event_detail', kwargs={'pk': self.id})


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('Moksha:person_detail', kwargs={'pk': self.id})
