list1=[3,6,9,12,15,18,21]
list2=[4,8,12,16,20,24,28]
r=list()
odd = list1[1::2]
print("Element at odd index position from list one")
print(odd)
even=list2[0::2]
print("Element at even index position from list two")
print(even)

print("Printing final third list")
r.extend(odd)
r.extend(even)
print(r)