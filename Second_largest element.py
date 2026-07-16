n=int(input("enetr the number of elemnets:"))
arr=[]
print("enetr the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
if n<2:
    print("array should contain ata least two elements.")
else:
    largest=second_largest=float('-inf')
    for num in arr:
        if num>largest:
            second_largest=largest
            largest=num
        elif num>second_largest and num !=largest:
            second_largest=num
    if second_largest == float('-inf'):
        print("there is no second largest element.")
    else:
        print("the second largest element is:",second_largest)
