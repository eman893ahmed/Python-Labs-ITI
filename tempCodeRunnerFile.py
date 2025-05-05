pyramid = []

def make_your_mario (num, in_py:list):
        for i in range(1, num+1):
                spaces = num - i
                stars = i
                in_py.append(' ' * spaces + '*' * stars)


        return in_py

out = make_your_mario(4,pyramid)
for i in range (4):
        print(pyramid)