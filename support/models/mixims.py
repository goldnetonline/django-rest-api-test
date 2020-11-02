'''
File: mixims.py
Project: token-credit-backend
File Created: Tuesday, 11th February 2020 1:14:33 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 2:09:03 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from random import sample, random
from django.db import models
from django.utils.text import slugify


class TouchDatesMixim(models.Model):
    '''
    Add created_at and updated_at support for models
    '''

    created_at = models.DateTimeField(
        'Date Created', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Date Updated', auto_now=True, null=True)

    class Meta:
        abstract = True

    @property
    def dateCreated(self):
        return self.created_at


class SlugifyMixim(models.Model):
    """
    Add a slug to the model
    """

    slug = models.SlugField(max_length=50, null=True,
                            blank=True, editable=False)

    class Meta:
        abstract = True

    def doSlug(self):
        if (hasattr(self, 'slug') and not self.slug) and \
                (hasattr(self, 'name') or hasattr(self, 'title')):
            toSlug = self.name if hasattr(self, 'name') else self.title
            self.slug = slugify(toSlug)
            self.save()

    def save(self, *args, **kwargs):
        self.doSlug()
        super().save(*args, **kwargs)


class RandomMixim:

    @classmethod
    def random(cls, pick: int = 3, **kwargs):
        try:
            pks = cls.objects.filter(**kwargs).values_list('pk', flat=True)
            if not pks:
                return None
            pk_sample = sample(list(pks), min(len(pks), pick))
            return sorted(cls.objects.filter(id__in=pk_sample, **kwargs), key=lambda _: random())
        except Exception:
            return None
