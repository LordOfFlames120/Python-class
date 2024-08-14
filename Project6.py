# Find even and odd numbers from a list, and store them separately in a new list
l=[5,18,38,12,15,47,39,20,13,46]
even=[]
odd=[]
for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
print("The even numbers are: ",even)
print("The odd numbers are: ",odd)