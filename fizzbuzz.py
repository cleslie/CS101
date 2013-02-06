def fizzbuzz(n):
    for i in range(n):
        if i!=0:
            if i%15==0:
                print("Fizzbuzz")
            elif i%3==0:
                print("Fizz")
            elif i%5==0:
                print("Buzz")
            else:
                print(i)

if __name__ == '__main__':
    fizzbuzz(20)
