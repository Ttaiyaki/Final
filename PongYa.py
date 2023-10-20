'''PongYa'''
def pongya(num):
    '''PongYa'''
    if int(num) % 3 == 0 or num[len(num)-1] == "3":
        print("PONG")
    else:
        print(num)
pongya(input())
