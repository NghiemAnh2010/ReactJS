def check_az(char1):
    if char1.islower() :
        return 0
    return 1
def check_AZ(char1):
    if char1.isupper():
        return 0
    return 1
def check_09(char1):
    if char1.isdigit():
        return 0
    return 1
def check_lenght(char1):
    if 6<=len(char1) and len(char1)<=12:
        return 1
    return 0
def check_char(char1):
    c1=['~','@','#','$','%','^','&','*',' ','"','?']
    for i in c1:
        if i in char1:
            return 1
    return 0