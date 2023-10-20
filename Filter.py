'''Filter'''
import json
def filtering(info, point):
    '''Filter'''
    info_dict = dict(sorted((json.loads(info)).items()))
    result = list(filter(lambda x: x >= point, info_dict.values()))
    status = True
    for i in info_dict.keys():
        if info_dict[i] in result:
            status = False
            print("{}{}{:.2f}".format(i, "\t", info_dict[i]))

    if status:
        print('Nope')
filtering(input(), float(input()))
