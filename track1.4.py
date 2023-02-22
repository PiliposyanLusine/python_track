#Given two integers a and b, return the sum of the two integers without using the operators + and -
a=int(input("Enter number1: "))
b=int(input("Enter number1: "))
def get_sum(a, b):
    while b:
        a, b = (a ^ b), (a & b) << 1
    return a
print (get_sum(a, b))
