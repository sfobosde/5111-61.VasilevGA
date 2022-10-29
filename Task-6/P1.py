import numpy as np

class dynamic_array:
    arr: np.ndarray
    capacity: int

    def __init__(self, capacity = 8, arr = None):
        if arr:
            self.arr = arr
        else:
            self.capacity = capacity
            arr = np.ndarray(self.capacity)
            print("Empty")


da = dynamic_array(np.ndarray(7))