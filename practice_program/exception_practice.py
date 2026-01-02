def fun(num):
    try:
        if num > 0:
            return 0
    except TypeError:
        raise TypeError("Enter only number")
    else:
        return 11
try:
    fun("vilas")
except TypeError as e:
    print(e)
    