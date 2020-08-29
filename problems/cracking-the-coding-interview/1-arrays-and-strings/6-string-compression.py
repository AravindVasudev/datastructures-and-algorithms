def compress_string(string):
    if not string:
        return string

    current_char = string[0]
    current_count = 0

    compressed = ''

    for char in string:
        if current_char == char:
            current_count += 1
        else:
            compressed += current_char + str(current_count)

            current_char = char
            current_count = 1

    compressed += current_char + str(current_count)

    return compressed if len(compressed) < len(string) else string


if __name__ == '__main__':
    assert compress_string('aabcccccaaa') == 'a2b1c5a3'
    assert compress_string('a') == 'a'
    assert compress_string('abcdef') == 'abcdef'
    assert compress_string('aabbcc') == 'aabbcc'
    assert compress_string('aaabbcc') == 'a3b2c2'
