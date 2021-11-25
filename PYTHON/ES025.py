numeri = [2,1,12,3,32,4]
massimo=numeri[1]
minimo=numeri[1]
for numero in numeri:
    if(numero>massimo):
        massimo = numero
    
    if(numero<minimo):
        minimo = numero

print(f"il minimo è {minimo}")  
print(f"il massimo è {massimo}")  