


def intersection(lst1, lst2):
    """[summary]

    Args:
        lst1 (list): first list
        lst2 (list): second list

    Raises:
        TypeError: lst1 argument must be a list
        TypeError: lst2 argument must be a list

    Returns:
        list: intersection of lst1 and lst2
    """
    if not isinstance(lst1, list):
        raise TypeError('lst1 argument must be a list')
    if not isinstance(lst2, list):
        raise TypeError('lst2 argument must be a list')
    # Use of hybrid method 
    temp = set(lst2) 
    lst3 = [value for value in lst1 if value in temp] 
    return lst3