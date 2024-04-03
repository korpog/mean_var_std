import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array([list[0:3], list[3:6], list[6:9]])
    mean = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.flatten().mean()]
    var = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.flatten().var()]
    std = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.flatten().std()]
    max = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.flatten().max()]
    min = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.flatten().min()]
    sum = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.flatten().sum()]
    
    calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum
        }


    return calculations