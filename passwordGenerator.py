import itertools


def Generate(type, longueur, maximum, combine):
    possibleCombo = longueur

    combinaisonsType = type

    speciaux = '!"#$%&\'()*+,-. /:;?@[]^_`{|}~'
    numeric = '0123456789'
    caractère = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if combinaisonsType == '1':
        getCaractère = numeric + caractère
    elif combinaisonsType == '2':
        getCaractère = numeric
    elif combinaisonsType == '3':
        getCaractère = caractère
    elif combinaisonsType == '4':
        getCaractère = speciaux
    elif combinaisonsType == '5':
        getCaractère = speciaux + numeric
    elif combinaisonsType == '6':
        getCaractère = speciaux + numeric + caractère
    elif combinaisonsType == '7':
        getCaractère = combine
    else:
        exit("Bad Input")

    maximal = maximum

    def generatePass(l):
        yield from itertools.product(*([l] * int(possibleCombo)))

    count = 0
    if maximal == "inf":
        for x in generatePass(getCaractère):
            f = open("passwordList.txt", "a")
            f.write(''.join(x) + "\n")
            count = count + 1
        f.close()
    else:
        for x in generatePass(getCaractère):
            f = open("passwordList.txt", "a")
            f.write(''.join(x) + "\n")
            count = count + 1
            if count >= int(maximal):
                break;
        f.close()
