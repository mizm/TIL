# class binaryTree :
#     def __init__(self, item) :
#         self.item = item
#         print(self.item)
#     def print(self):
#         print(self.item)

# a = binaryTree(51)
# a.print()
def fib_loop(n) :
    
    f1 = 1
    f2 = 1
    temp = 0
    if n == 0 or n == 1 :
        return 1
    for i in range(n-1) :
        temp = f1 + f2
        f2 = f1
        f1 = temp
    return temp

print(fib_loop(10))