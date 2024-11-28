import inspect


def introspection_info(x):
    typ = type(x).__name__
    met = []
    att = []
    for i in dir(x):
        if i[:2] == "__":
            met.append(i)
        else:
            att.append(i)
    mod = inspect.getmodule(x).__name__ if inspect.getmodule(x) else '__main__'
    return {"type": typ, "attributes": att, "methods": met,"module": mod}



number_info = introspection_info(42)
print(number_info)