def digit_root(num):

    root = 0
    num_str = str(num)

    for i in range(0, len(num_str)):
        digit_str = num_str[i]
        digit = int(digit_str, 10)
        root += digit

    if root < 10:
        return root
    else:
        return digit_root(root)


print(digit_root(1))
print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))
print(digit_root(9999999))
