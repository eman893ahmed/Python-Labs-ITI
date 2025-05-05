def normal_multiplication(x):
    for i in range(1, x + 1):
        for j in range(1, i + 1):  
            return i * j
            
x = int(input("Enter your number: "))
print(normal_multiplication(x))
