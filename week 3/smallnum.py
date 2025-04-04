def small(li):
    small=li[0]
    for i in range(1,len(li)):
        if li[i]<small:
                small=li[i]
    return small
    
def print_list(li):
        for i in li:
                print(i,end=" ")
                
                
elements=[]
limit=int(input("enter the limit for list:"))
for i in range(limit):
    val=int(input("enter value:"))
    elements.append(val)
print("elements in the list are")
print_list(elements)

print()

print(" the smallest element is =",small(elements))
