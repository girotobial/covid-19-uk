# base.py
# Defines base class for all plots

from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class ABCPlot(ABC):
    def __init__(self, figsize=None):
        if figsize is None:
            figsize = (9.75, 6)
        fig, ax = plt.subplots(figsize=figsize)
        self.fig = fig
        self.ax = ax

    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def save(self):
        pass
