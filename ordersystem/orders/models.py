from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class Order(models.Model):
    """Job Order"""

    ticket = models.CharField(_('ticket'), max_length=200)

    class Meta:
        ordering = ['ticket',]
        verbose_name, verbose_name_plural = "Order", "Orders"

    def __unicode__(self):
        return "%s" % (self.ticket)

    @models.permalink
    def get_absolute_url(self):
        return ('')