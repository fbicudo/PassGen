import time

def replace(originalLowCase, originalCapital, replacement, originalList):

    newv = []
    for p in originalList:
        # print(p)
        if p.find(originalLowCase) or p.find(originalCapital):
            newp = p.replace(originalLowCase, replacement)
            newp = newp.replace(originalCapital, replacement)
            # print(newp)
            newv.append(newp)
    originalList.extend(newv)
    newv = list(dict.fromkeys(originalList))
    originalList = newv
    return(originalList)


def capitalize(originalList):

    pwdlenght = len(originalList[0])

    tmpList = []

    for p in originalList:
        pwdlenght = len(p)
        pwd = str(p)

        # Code portion to change cases
        while pwdlenght > 0:
            for i in range(0,pwdlenght):
                if pwd[i].isnumeric() == False:
                    pwd = pwd[0:i].lower() + pwd[i].upper() + pwd[i+1:]
                    tmpList.append(pwd)
            pwdlenght = pwdlenght - 1
    
    originalList.extend(tmpList)
    originalList = list(dict.fromkeys(originalList))

    return(originalList)


def doVariations(originalList):

    originalList = replace("a", "A", "@", originalList)
    originalList = replace("a", "A", "4", originalList)
    originalList = replace("e", "E", "3", originalList)
    originalList = replace("i", "I", "!", originalList)
    originalList = replace("i", "I", "|", originalList)
    originalList = replace("l", "L", "1", originalList)
    originalList = replace("c", "C", "(", originalList)
    originalList = replace("o", "O", "0", originalList)
    originalList = replace("t", "T", "7", originalList)
    originalList = replace("s", "S", "5", originalList)
    originalList = replace("s", "S", "$", originalList)
    originalList = replace("g", "G", "9", originalList)
    originalList = capitalize(originalList)

    return(originalList)


if __name__ == "__main__":

    origin_pwd = "password"
    variations = []

    temp = []

    pwd = origin_pwd.lower()
    variations.append(pwd)

    print(variations)
    variations = doVariations(variations)
    print(f"A total of {len(variations)} variations:")
    print(variations)