def outer(ref):
    def inner(a,b):
        print(a+b)
        ref(a,b)
    return inner
@outer
def add(a,b):
    print(a-b)

add(int(input("enter the number ")),int(input("enter the numer2")))