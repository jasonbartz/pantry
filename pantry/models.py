'''
This stores the Modeling objects
'''
# Standard Library
import datetime

# Django
from django.db import models

# Pantry
from pantry.measurement.models import MeasurementType

class BaseModel(models.Model):
    created             = models.DateTimeField(auto_now_add=True)
    modified            = models.DateTimeField(auto_now=True)
    name                = models.CharField()
    slug                = models.CharField()

class Group(BaseModel):
    '''
    A normalized grouping of similar (read: interchangeable) items
    '''
    grouping_type

class Item(BaseModel):
    '''
    A normalized class for dealing with individual items.

    Can be grouped together using the Group class.

    For example, a particular box of pasta can be represented as an Item,
        but all of the pastas can be grouped together as Pasta, because they are,
        most likely, fairly interchangeable.
    '''
    group               = models.ForeignKey(Group, null=True)
    measurement_type    = models.ForeignKey(MeasurementType, null=True)
    amount              = models.CharField()
