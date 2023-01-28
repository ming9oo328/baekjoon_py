jusawii = {1:'Yakk', 2:'Doh', 3:'Seh', 4:'Ghar', 5:'Bang', 6:'Sheesh'}
same = {1:'Habb Yakk', 2:'Dobara', 3:'Dousa', 4:'Dorgy', 5:'Dabash', 6:'Dosh'}
T = int(input())

for i in range(T):
    sang,chang = map(int,input().split())
    if (sang == 6 and chang == 5) or (sang == 5 and chang == 6):
        word = "Sheesh Beesh"
    elif(sang>chang):
       word = jusawii[sang]+" "+jusawii[chang]
    elif(sang<chang):
        word = jusawii[chang]+" "+jusawii[sang]
    else:
        word = same[sang]
    print("Case "+str(i+1)+": "+word)