def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict['i'])
    print(dict['s'])
    print(dict['p'])
    print(dict['M'])
    return "End OF PROGRAM"
print(char_frequency('Mississippi'))
print()
