# base.py
# Defines base class for all plots

from abc import ABC, abstractmethod
import matplotlib as mplt

class ABCPlot(ABC):
    def __init__(self, figsize=None):
        if figsize is None:
            figsize = (9.75, 6)
        self.fig = mplt.figure.Figure()
        self.ax = mplt.axes.Axes()

    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def show(self):
        pass

    def save(self, path):
        self.fig.savefig(path)
