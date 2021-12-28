def hawkID():
    return "lldeng"

def q1(numerator, denominator):
    num = numerator
    denom = denominator
    denomList = []
    currentDenom = 1
    while num != 0:
        if denom <= currentDenom * num:
            num = (currentDenom * num) - denom
            denom = denom * currentDenom
            denomList.append(currentDenom)
        currentDenom = currentDenom + 1
    equation = "{}/{} = ".format(numerator, denominator)
    i = 0
    while i < len(denomList):
        if i == len(denomList) - 1:
            equation = equation  + "1/{}".format(denomList[i])
        else:
            equation = equation  + "1/{} + ".format(denomList[i])
        i = i + 1
    print(equation)
    return denomList

