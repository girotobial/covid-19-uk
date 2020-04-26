# Growth Factor.py
# Defines the GrowthFactor plot class

from .base import ABCPlot
from ..calc import growth_ratio


class GrowthFactor(ABCPlot):
    def __init__(self, date_col, cases_col,  data=None):
        self._dates_col = date_col
        self._cases_col = cases_col
        self.data = data
        super().__init__()

    def _growth_ratio(self):
        return growth_ratio(self._cases_col)
    
    def _parse_inputs(self):
        # TODO
        pass

    def plot(self):
        # TODO
        pass

    def show(self):
        # TODO
        pass


def plot_growth_factor():
    '''
    A wrapper around the growth factor class
    '''
    # TODO
    pass