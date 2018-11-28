def fuc(type_ = 's'):
    if type_ == 's':
        return 'Mark'
    elif type_ == 'i':
        return  20

def dec (fuc, type_):
    x = 8
    def wrapper ():
        value = fuc(type_)
        if isinstance(value, int):
            return value * x
        elif isinstance(value, str):
            return 'dasdas'

    return wrapper()
print(dec(fuc, 'i'))
