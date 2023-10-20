'''Easy Histogram'''
def sorting(histogram):
    '''sorting'''
    for char in histogram:
        if char.isupper():
            return ord(char.lower()) + 0.5
        else:
            return ord(char)

def easy_histogram(text):
    '''Easy Histogram'''
    histogram = {}
    for i in text:
        if i == ' ':
            continue
        if i not in histogram:
            histogram.update({i: 1})
        else:
            histogram[i] += 1

    histogram = dict(sorted(histogram.items(), key=sorting))
    for key in histogram.keys():
        print(key, '=', histogram[key])
easy_histogram(input())
