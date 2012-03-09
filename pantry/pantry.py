'''
The base class object from which all Pantry functionality is derived.

For web views, see views.py

for urls, see urls.py

for modeling, see documents.py (uses mongo, so the standard models.py will not apply)
'''

class Pantry(object):
    
    def __init__(self, *args, **kwargs):
        
        self.args = args
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    