def compact(lst):
    new_list = []
    for item in lst:
        if item:
            new_list.append(item)
    return new_list
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """