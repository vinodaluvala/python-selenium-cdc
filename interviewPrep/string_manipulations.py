def string_mani():
    n = input("Enter a string: ")
    li = n.split()
    hm = {}
    for i in li:
        if i in hm:
            hm[i]+=1
        else:
            hm[i] = 1
    print(hm)
string_mani()

# Conversion of two list into Dictionary Using Python

def list_to_dict():
    x = [1, 2, 3]
    y = ["one", "Two", 'Three']
    result = dict(zip(x, y))
    print(result)
list_to_dict()

def dict_to_list():
    x = {1: 'one', 2: 'Two', 3: 'Three'}
    for i in x.items():
        print(list(i))
dict_to_list()