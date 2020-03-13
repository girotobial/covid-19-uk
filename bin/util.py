import numpy as np

def divide(num, denum, err):
    if denum > 0:
        return num / denum
    else:
        return err