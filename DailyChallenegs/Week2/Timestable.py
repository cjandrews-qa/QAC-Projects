n=int(input('Enter a Number: '))
def timet(n):
    line = ""
    for hori in range(1,n+1):
        for vert in range(2,n+1):
            line = line + str((hori*vert)) + "\t"
        line += "\n"
    return line
print(timet(n))
        


     