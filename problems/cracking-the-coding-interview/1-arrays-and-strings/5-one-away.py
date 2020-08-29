def is_one_away(str1, str2):
    i, j = 0, 0
    isEdited = False

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if isEdited:
                return False

            # Insertion
            if str1[i] == str2[j + 1]:
                i += 1

            # Deletion
            elif str1[i + 1] == str2[j]:
                i += 1

            # Updation
            elif str1[i + 1] == str2[j + 1]:
                i += 1
                j += 1

            isEdited = True
        else:
            i += 1
            j += 1

    return True

if __name__ == '__main__':
    assert is_one_away('pale', 'ple') == True
    assert is_one_away('pales', 'pale') == True
    assert is_one_away('pale', 'bale') == True
    assert is_one_away('aaaa', 'aaa') == True
    assert is_one_away('pale', 'bake') == False
