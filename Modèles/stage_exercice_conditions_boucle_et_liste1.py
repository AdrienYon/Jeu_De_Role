nombres = range(10)
nombres_inverse = [ i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverse)