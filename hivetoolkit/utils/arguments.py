""" argument's type checking tools """


def checkList(arg_list, name_arg, type_inside_arg=str):
    """Check if arg_list is an instance of list and if every variable inside arg_list is an instance of type_inside_arg

    Args:
        arg_list (list(type_inside_arg)): arg to check
        name_arg (str): name of the argument, asked to complete Error explanation
        type_inside_arg (type, optional): supposed type of the variables inside arg_list. Defaults to str.

    Raises:
        TypeError: IF NOT type(arg_list) IS list
        TypeError: IF NOT type(arg_list[x]) IS type_inside_arg
    """
    type_arg = list
    str_type_arg = type_arg.__name__
    str_type_inside_arg = type_inside_arg.__name__

    if not isinstance(arg_list, type_arg):
        raise TypeError(
            "{} argument must be an instance of {}".format(name_arg, str_type_arg)
        )
    for elem in arg_list:
        if not isinstance(elem, type_inside_arg):
            raise TypeError(
                "{} argument must contain only instances of {}".format(
                    name_arg, str_type_inside_arg
                )
            )
