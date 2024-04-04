import numpy as np

def age_map(x: int) -> str:
    """
    Returns the age group of a particular passenger
    given their age.
    
    Args
    age [int] : The age in integer
    
    Return
    age_group [str] : The age group based on the given age.
    """
    age_group = ""
    x = int(x)
    
    if x < -1:
        raise ValueError(f"Invalid Argument { x } in func: ")

    if x in np.arange(0, 10):
        age_group = "chidren"
    elif x in np.arange(10, 18):
        age_group = "adolescent "
    elif x in np.arange(18, 25):
        age_group = "youth"
    elif x in np.arange(25, 35):
        age_group = "young adult"
    elif x in np.arange(35, 50):
        age_group = "adult"
    elif x in np.arange(50, 65):
        age_group = "older adult"
    elif x >= 65:
        age_group = "Old Age"
    elif x == -1:
        age_group = "not available"
    else:
        raise ValueError(f"Invalid Argument { x } in func: ")
    return age_group

    
    
    