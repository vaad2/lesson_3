from django.db import models
from django.utils.translation import ugettext_lazy as _


class Template(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    content = models.TextField(verbose_name=_('content'))
    status = models.BooleanField(verbose_name=_('status'), default=False)

    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')
