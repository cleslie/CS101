potential_prime = -1
primeList=[]

while potential_prime < 1999: 
    potential_prime += 2 
    is_prime = True
    for i in range(2,potential_prime): 
        if potential_prime % i == 0: 
            is_prime = False 
            break 
    if is_prime == True: 
        primeList.append(potential_prime)

print(primeList)

