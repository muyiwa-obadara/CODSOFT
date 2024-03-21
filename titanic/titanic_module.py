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
    
    if x < 0:
        raise ValueError(f"Invalid Argument { x } in func: ")
    
    if x in np.arange(0, 18):
        age_group = "chidren"
    elif x in np.arange(18, 45):
        age_group = "youth"
    elif x in np.arange(45, 65):
        age_group = "adult"
    elif x in np.arange(65, 120):
        age_group = "old age"
    else:
        raise ValueError(f"Invalid Argument { x } in func: ")
    return age_group
    
    