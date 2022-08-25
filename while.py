

n = 0
cont = 0
arr = []
contNeg = 0
sumNeg = 0
while cont < 3:
    n = int(input('Digite un numero: '))

    if n < 0:
        contNeg += 1      
        sumNeg += n
           
    cont += 1  
   
    

print(f'Hay {contNeg} numeros negativos')
print(f'Los suma de los negativos es: {sumNeg}')




   




         
  
