# base.py
# Defines base class for all plots

from abc import ABC, abstractmethod

class ABCPlot(ABC):
    def __init__(self, dataframe):
        self.df = dataframe
    
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def save(self):
        pass
