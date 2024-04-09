def species_map(specie_name: str):
    """Takes the names of a specie and maps
    it into an integer.
        Iris-setosa        0
        Iris-versicolor    1
        Iris-virginica     2
        
    Args
    specie_name (str) A The specie of the Iris flower
    
    Return
    specie_code (int) 0, 1, or 2
    
    Example
    >>> species_map("Iris-setosa")
    [out] 0
    """
    if specie_name == "Iris-setosa":
        return 0
    elif specie_name == "Iris-versicolor":
        return 1
    elif specie_name == "Iris-virginica":
        return 2
    else:
        raise ValueError(f"Invalid Specie { specie_name }")