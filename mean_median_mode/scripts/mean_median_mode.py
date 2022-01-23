import statistics
import numpy as np
userinput = input('Dame una lista: ')
lista = userinput.split()

for count, value in enumerate(lista):
    lista[count] = float(lista[count])

sorted_list = sorted(lista)

# Total de elementos y lista ordenada
print(f'\nTu lista tiene {len(lista)} elementos')
print(f'Aquí tienes tu lista ordenada: {sorted_list}')

# Media
print(f'La media de tu lista es: {(np.mean(sorted_list))}')

# Mediana
print(f'La mediana de tu lista es {np.median(sorted_list)}')

# Moda
if len(sorted_list)% 2 == 0:
    print(f'La moda de tu lista es: {statistics.multimode(sorted_list)}')
else:
    counts = np.bincount(sorted_list)
    print(f'La moda de tu lista es: {np.argmax(counts)}')

# Desviación Estándar
print(f'La desviación de tu lista es {np.std(sorted_list)}')
