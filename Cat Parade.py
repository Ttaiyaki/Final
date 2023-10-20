'''Cat Parade'''
def parade():
    '''Cat Parade'''
    cat_pa = []
    cat_dict = {}
    while True:
        cat = input().split(", ")
        if cat == ["END"]:
            break
        cat_pa.extend(cat)
        if "IT'S A DOG" in cat:
            del cat_pa[len(cat_pa)-2: len(cat_pa)]
            continue

    for cat in cat_pa:
        if cat in cat_dict:
            continue
        cat_dict.update({cat: cat_pa.count(cat)})

    cat_dict = dict(sorted(cat_dict.items()))
    for key in cat_dict:
        print(key, cat_pa.index(key)+1, cat_dict[key])
parade()
