n = input('Ingrese un numero => ')
c = 0

dimension = len(n)
print(dimension)

if 2 < dimension < 8:
    for i in n:
        if i == '5':
            print('Salto')
            c += 1 
        else:
            print(i)
    print(f'Numero iguales a 5 => {c}')
    print(f'Numeros diferntes a 5 => {dimension - c}')
    print(f'total de digitos =>  {dimension}')
else:
    print('Error, fuera de rango')
