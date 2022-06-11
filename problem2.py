#valid parenthesis
def balaced_parenthesis(parenthesis):
    x= 0
    output=False
    for i in parenthesis:
        if i == "(":
            x += 1
        elif i == ")":
            x-= 1
        if x < 0:
            return output
    if x==0:
        return not output
    return output
    



s=[]
print(balaced_parenthesis(s))

y="a()a[]x{}p "
print(balaced_parenthesis(y))

k="(]y"
print(balaced_parenthesis(k))
