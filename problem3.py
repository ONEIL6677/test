# a function that returns indidces of two numbers such that they add up to target

def sum_up_to_target(list1):
    target=8
    for x in range(len(list1)):
        for y in range(x+1, len(list1)):
            if list1[x]+list1[y]==target:
                return [x,y]
        
    else:
        return f"list is empty"
                



y="ghtrjyt"
print(sum_up_to_target(y))

