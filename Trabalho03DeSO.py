import random
import numpy as np

x = []

for i in range(1000):
    num = random.randint(0, 9)
    x.append(num)
    
#print(x)

with open('numeros.txt', 'w') as stream:
    for i in x:
        stream.writelines(f'{i}\n')


#Algoritmo de envelhecimento
Capacidade = 4
ListaDeProcessos = x              
aux = []
pageFaults = 0
for i in ListaDeProcessos:
    if i not in aux:
        if(len(aux) == Capacidade):
            aux.remove(aux[0])
            aux.append(i)
        else:
            aux.append(i)
        pageFaults +=1
 
    else:
        aux.remove(i)
        aux.append(i)
     
print(f"Envelhecimento: {pageFaults}", end=" - ")

# LIFO
from queue import Queue 
   
def pageFaults(paginas, n, capacidade):
    aux = set()  
    indexes = Queue()  
    page_faults = 0
    for i in range(n):
        if (len(aux) < capacidade): 
            if (paginas[i] not in aux):
                aux.add(paginas[i]) 
                page_faults += 1
                indexes.put(paginas[i]) 
        else:
            if (paginas[i] not in aux):
                val = indexes.queue[0] 
                indexes.get()  
                aux.remove(val) 
                aux.add(paginas[i])  
                indexes.put(paginas[i]) 
                page_faults += 1
  
    return page_faults
paginas = x 
n = len(paginas) 
capacidade = 4
pageFaults2 = pageFaults(paginas, n, capacidade)

print(f"LIFO: {pageFaults2}")

  
 
