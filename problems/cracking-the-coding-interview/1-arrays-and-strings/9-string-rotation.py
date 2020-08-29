def checkRotation(str1, str2):
    return str1 in (str2 + str2)

if __name__ == '__main__':
    assert checkRotation('waterbottle', 'erbottlewat') == True
    assert checkRotation('waterbottle', 'erbottlewate') == False
