n=int(input("enter the number of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
total = 0
for i in range(n):
    total = total + arr[i]
print("Sum of all elements:",total)
