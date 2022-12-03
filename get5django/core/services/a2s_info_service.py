
from django import forms
from service_objects.services import Service
import a2s
import logging
import socket 

logger = logging.getLogger(__name__)

class A2sInfoService(Service):
    address = forms.CharField()

    def process(self):
        logger.debug('executing a2s info service')
        
        address = self.cleaned_data['address']
        
        if ":" not in address:
            address = f'{address}:27015'

        server, port = address.split(':')

        try:
            # Get
            info = a2s.info((server, int(port)))
            # To Dict
            info_dict = {}
            for attr in dir(info):
                if attr.startswith('_'):
                    continue
                info_dict[attr] = getattr(info, attr)
            info = info_dict
        except socket.timeout as e:
            logger.warn('Info Timeout')
            info = None
        
        return info

