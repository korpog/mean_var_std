import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array([list[0:3]], [list[3:6], list[6:9]])
    print(arr)
    means = [arr.me]
    calculations = {}


    return calculations