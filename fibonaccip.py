#fib sequence
def fibonacci(num):
    terms = [0,1]
    i = 2
    while i<=num:
        terms.append(terms[i-1] + terms[i-2])
        i = i+1
    return terms[num]

user_input=int(input("Enter a number to find the corresponding number in the fibanacci sequence: "))

print(fibonacci(user_input))   

