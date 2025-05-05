def normal_mario():
        for i in range(1, 5):
                spaces = 5 - i
                stars = i
                return ' ' * spaces + '*' * stars

print(normal_mario())