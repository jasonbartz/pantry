"""
documents.py

The data models for the app (MongoDB)

"""
# Standard Library
import datetime

# Django
from mongoengine import Document, fields

# Pantry
from pantry.measurement.models import MeasurementType

class BaseDocument(Document):
    created             = fields.DateTimeField(default=datetime.datetime.now())
    modified            = fields.DateTimeField(default=datetime.datetime.now())
    name                = fields.StringField()
    slug                = fields.StringField()

# class Group(BaseDocument):
#     '''
#     A normalized grouping of similar (read: interchangeable) items
#     '''
#     grouping_type

class Item(BaseDocument):
    '''
    A normalized class for dealing with individual items.

    Can be grouped together using the Group class.

    For example, a particular box of pasta can be represented as an Item,
        but all of the pastas can be grouped together as Pasta, because they are,
        most likely, fairly interchangeable.
    '''
    # group               = models.ForeignKey(Group, null=True)
    # measurement_type    = models.ForeignKey(MeasurementType, null=True)
    # amount              = models.CharField()
