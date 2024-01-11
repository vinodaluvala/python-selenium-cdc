def string_mani():
    n = input("Enter a string: ")
    li = n.split()
    hm = {}
    for i in li:
        if i in hm:
            hm[i]+=1
        else:
            hm[i] = 1
    print(hm.get())
string_mani()