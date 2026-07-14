n=int(input("enetr the number of elements"))
arr=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
smallest=arr[0]
for i in range(1,n):
    if arr[i]<smallest:
        smallest=arr[i]
print("the smallest element is:",smallest)
    
