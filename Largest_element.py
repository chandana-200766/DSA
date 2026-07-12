n=int(input("Enter the number of elements: "))
arr=[]
print("Enter the elements: ")
for i in range(n):
    element=int(input())
    arr.append(element)
largest=arr[0]
for i in range(1,n):
    if arr[i]>largest:
        largest=arr[i]
print("The largest element is:",largest)
