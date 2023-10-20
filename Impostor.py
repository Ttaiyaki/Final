'''Impostor'''
import json
def amongus():
    '''Impostor'''
    member_dict = {}
    while True:
        member = input()
        if member == "Start":
            break
        member_dict.update(json.loads(member))

    voteout_dict = {}
    while True:
        vote = input()
        if vote == "End":
            break
        if vote in member_dict:
            voteout_dict.update({vote: member_dict.pop(vote)})

    count_impostor = 0
    for i in member_dict.values():
        if i == "Impostor":
            count_impostor += 1

    print("{} Impostor Remains".format(count_impostor))
    print("***Alive***")
    for key in dict(sorted(member_dict.items())):
        print(key + ' : ' + member_dict[key])

    print("***Dead***")
    for key in dict(sorted(voteout_dict.items())):
        print(key + " : " + voteout_dict[key])
amongus()
