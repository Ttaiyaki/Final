'''iPad Air'''
def ipad(color_picked, storage_picked, wifi_picked):
    '''iPad Air'''
    color = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    storage = [64, 256]
    wifi = ["Wi-Fi", "Wi-Fi + Cellular"]
    if color_picked in color and storage_picked in storage and wifi_picked in wifi:
        print(price(storage_picked, wifi_picked))
    else:
        print("Not Available")

def price(storage, wifi):
    '''ipad price'''
    if storage == 64:
        if wifi == "Wi-Fi":
            return 19900
        else:
            return 24400
    else:
        if wifi == "Wi-Fi":
            return 24900
        else:
            return 29400

ipad(input(), int(input()), input())
