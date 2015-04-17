from django.core.validators import MinValueValidator
from django.core.urlresolvers import reverse
from django.db import models

class RedPanda(models.Model):

    name = models.CharField(max_length=50)
    cuteness = models.IntegerField(validators=[MinValueValidator(3)])

    def say_something_cute(self):
        return "<3" * self.cuteness

    def get_absolute_url(self):
        return reverse('redpanda-detail', args=[self.name])
