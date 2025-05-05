result_list_out = []

def list_multiplication(x):
    for i in range(1, x + 1):
        result_list_in = []
        for j in range(1, i + 1):  
            value = i*j
            result_list_in.append(value)
        result_list_out.append(result_list_in)

    return result_list_out

x = int(input("Enter your number: "))
print(list_multiplication(x))