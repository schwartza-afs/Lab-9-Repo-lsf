
def encode(password):
    encoded = ""
    for i in password:
        if i == "7":
            num = 0
        elif i == "8":
            num = 1
        elif i == "9":
            num = 2
        else:
            num = int(i)
            num += 3
        encoded += str(num)
    return encoded