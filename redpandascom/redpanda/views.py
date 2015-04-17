from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from redpanda.models import RedPanda


class RedPandaCreate(CreateView):
    model = RedPanda
    fields = ['name', 'cuteness']


class RedPandaDetail(DetailView):
    model = RedPanda
    slug_field = 'name'
    slug_url_kwarg = 'name'
