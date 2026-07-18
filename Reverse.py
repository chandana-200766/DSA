n=int(input("enetr a number:"))
arr=[]
print("Enter the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
start = 0
end = n-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
print("Reversed array is:")
for i in range(n):
    print(arr[i],end=" ")
