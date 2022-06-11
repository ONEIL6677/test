
def palindrom(myparl):
    ispalindrom=list(reversed(myparl))==list(myparl)
    return ispalindrom



x="aba"
print(palindrom(x))