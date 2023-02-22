#Given an integer array nums,
#return true if any value appears at least twice in the array,
#and return false if every element is distinct.
list = input("Enter numbers for list: ")
list1 = ""
for int in list:
    if int not in list1:
        list1=list1+int
if (list1 == list):
    print(" True ")
else:
        print(" False ")
