#Write a function that takes the binary representation
# of an unsigned integer and returns the number of '1' bits it has
num=int(input("Enter unsigned integer number: "))
def bin_dec(num):
    bin = 0
    num2 = 0
    while num != 0:
        if num % 10 == 1:
            bin += 2 ** num2
        num2 += 1
        num //= 10
    return bin
print(bin_dec(num)) 
