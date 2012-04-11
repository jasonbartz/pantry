'''
This stores the Modeling objects, used in particular for modeling
measurement networks
'''
from mongoengine import fields
from mongoengine import Document

class Measurement(Document):
    '''
    A document that represents an individual measurement
        that is part of the network
    '''
    measurement_type_id             = fields.IntField()
    
class MeasurementNetwork(Document):
    '''
    A Mongo document that simulates a lightweight network
        graph for a group of measurements
    '''
    # The ISO to which the Measurement Network belongs
    measurement_iso_id              = fields.IntField()
    
    # Baseline measurement is always 1 in this network
    baseline_measurement_id         = fields.IntField()
    
    # This maps the measurements in the increased direction
    # increase_ratio is the ratio by which a measurement must
    #   increase in order to get to the next measurement
    increase_ratio                  = fields.FloatField()
    # A sorted list of measurements on the increasing line
    #   0 index is the smallest, (n) is the largest
    measurements_increased          = fields.SortedListField()
    
    # decrease_ratio is the ratio by which a measurement must
    #   decrease in order to get to the next measurement
    decrease_ratio                  = fields.FloatField()
    # A sorted list of measurements on the increasing line
    #   0 index is the largest, (n) is the smallest
    measurements_decreased          = fields.SortedListField()

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
    size_meta           = fields.StringField()
    
    # Kind of measurement, US, Metric, UK
    #iso    