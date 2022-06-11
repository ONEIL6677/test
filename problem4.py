
def devid(mylist):
    total=sum(mylist)
    halftotal=sum(mylist)//2
    for elem in mylist:
        if total//elem==halftotal:
            return elem
    # else:
    #     mylist=[]
    #     return "list is empty"        


y=[1,4,2,5]
print(devid(y))
x=[2,3,4,5,6,7,8,9,9]
print(devid(x))

