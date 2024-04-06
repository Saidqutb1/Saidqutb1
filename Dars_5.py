def a():
    b = 1

    def inner():
        print(b)

    return inner
func = a()
func()









