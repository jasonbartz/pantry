'''
This is the module for scanning UPCs
'''
import StringIO

import Image
import zbar
import requests

from pantry.exceptions import NotSupported

class UPCScanner(object):
    
    def __init__(self, *args, **kwargs):
        
        self.args = args
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def get(self, image_location, location_type='file'):
        '''
        Public Method for loading an image and returning
            a dictionary containing upc information
        '''
        raw_image_str = self.load_image(image_location, 
                                        location_type=location_type)
                                        
        upcs = self.scan_image(raw_image_str)
        
        return upcs
    
    def load_image(self, image_location, location_type='file'):
        '''
        Public method for loading an image containing a
        UPC into PIL
        
        Required Params
        :: image_location
        Local or web address where the image is stored
        
        :: location_type
        Determines how UPCScanner will retrieve image.
        Currently supported: file, web
        '''
        image_object = self._open_image(image_location, 
                                        location_type=location_type)
        return image_object
        
    def scan_image(self, image_object):
        '''
        Public method for scanning an image and retrieving
            UPC or UUC codes
        '''
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        
        raw_image_str, width, height = self._convert_image_to_raw(image_object)
        
        image = self._convert_for_zbar(raw_image_str, width, height)
        
        scanner.scan(image)
        upc_list = []
        
        for symbol in image:
            upc_list.append({
                'type': symbol.type,
                'data': symbol.data,
                'location': symbol.location,
                'quality': symbol.quality, 
            })
        return upc_list
        
    def _open_image(self, image_location, location_type='file'):
        '''
        Open an image and return an image object
        '''
        if location_type == 'file':
            with open(image_location, 'rb') as image_file:
                image = Image.open(image_file).convert('L')
                
                return(image)
                
        elif location_type == 'web':
            response = requests.get(image_location)
            
            if response.status_code == requests.codes.ok:
                image = Image.open(StringIO(respnse.content))
                
                return(image)
            
            else:
                raise RetrievalError('Could not get image, response: %s' % \
                                    response.status_code)
        else:
            raise NotSupported('Current location_type %s is not supported' % \
                                location_type)
                                
    def _convert_image_to_raw(self, image_object):
        '''
        Convert the Image object to raw
        '''
        width, height = image_object.size
        raw = image_object.tostring()
        
        return raw, width, height

    def _convert_for_zbar(self, raw_image_str, width, height):
        
        image = zbar.Image(width, height, 'Y800', raw_image_str)
        return(image)