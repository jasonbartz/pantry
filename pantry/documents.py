'''
This stores the Document modeling objects
'''
# Standard Library
import datetime

# MongoEngine
from mongoengine import Document
from mongoengine import fields

class BaseDocument(Document):
    created         = fields.DateTimeField(default=datetime.datetime.now())
    modified        = fields.DateTimeField(default=datetime.datetime.now())
    name            = fields.StringField()
    slug            = fields.StringField()

class Item(BaseDocument):
    '''
    A normalized class for dealing with individual items.
    
    Can be grouped together using the Group class.
    
    For example, a particular box of pasta can be represented as an Item,
        but all of the pastas can be grouped together as Pasta, because they are,
        most likely, fairly interchangeable.
    '''
    pass
    
class Group(BaseDocument):
    '''
    A normalized grouping of similar (read: interchangeable) items
    '''
    pass
    
class Measurement(BaseDocument):
    '''
    A normalized representation of a measurement, eg. milliliters. 
    
    The actual amount is represented at the item level.
    '''
    pass
    
