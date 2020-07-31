""" argument's type checking tools """


def check_arg(arg, arg_type, arg_name, sub_type=None):

    str_arg_type = arg_type.__name__
    if sub_type != None:
        str_sub_type = sub_type.__name__

    if not isinstance(arg, arg_type):
        raise TypeError(
            "{} argument must be an instance of {}".format(arg_name, str_arg_type)
        )
    try:
        iter(arg)
    except TypeError:
        pass
    else:
        for elem in arg:
            if not isinstance(elem, sub_type):
                raise TypeError(
                    "{} argument must contain only instances of {}".format(
                        arg_name, str_sub_type
                    )
                )
