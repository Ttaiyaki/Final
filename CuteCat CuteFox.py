'''CuteCat CuteFox - error 1 case'''
def count(dicted):
    '''count'''
    count_cat = 0
    count_fox = 0
    for i in dicted.values():
        if "Cat" in i:
            count_cat += 1
        else:
            count_fox += 1
    return count_cat, count_fox

def catfox(num):
    '''CuteCat CuteFox'''
    animaldict = {}
    for _ in range(num):
        animal = input().split(" : ")
        if "Cat" != animal[1][1:-4].title() and "Fox" != animal[1][1:-4].title():
            continue

        if animal == '':
            continue
        animaldict.update({animal[0][2:-1]: animal[1][1:-2]})

    if not "Cat01" in animaldict.values() and not "Garfield" in animaldict.keys():
        animaldict.update({"Garfield": "Cat01"})
    if not "Fox01" in animaldict.values() and not "Fubuki" in animaldict.keys():
        animaldict.update({"Fubuki": "Fox01"})

    animal_sort = dict(sorted(animaldict.items(), key=lambda x: x[1].title()))

    print("Cat : {}\nFox : {}".format(*count(animal_sort)))
    for i in animal_sort:
        print(i, ":", animal_sort[i])
catfox(int(input()))
