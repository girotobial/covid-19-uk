# config.py
# Class to hold configuration of plots

from .abc_config import ABCConfig

class PlotConfig(ABCConfig):
    '''Stores configuration information for plots'''
    def __init__(self):
        self.figsize = None,
        self.style = None
        self.font = None
        self.font_size = None
    
    def read_file(self, path, section: str):
        config = self._open_config_file(path, section)
        
        self.figsize = (
            config.getfloat('figure height'),
            config.getfloat('figure width')
        )
        
        self.style = config.get('style')
        self.font = config.get('font')
        self.font_size = config.get('font size')
        return self
