'''
This stores the Modeling objects for measurements
'''
from pantry.models import BaseModel
from django.db import models

class MeasurementISO(BaseModel):
    '''
    Represents a category of measurement
    '''
    pass
    
class MeasurementType(BaseModel):
    '''
    A normalized representation of a measurement, eg. milliliters. 
    
    The actual amount is represented at the item level.
    '''
    # Volume, Weight, etc.
    size_meta           = models.CharField(null=True, blank=True)
    
    # Kind of measurement, US, Metric, UK
    iso                 = models.ForeignKey(MeasurementISO)