def hash_function(obj):
    obj = str(obj)
    total1 = total2 = 0

    for i in range(len(obj) // 2):
        if len(obj) % 2 != 0 and i == (len(obj) // 2) - 1:
            total1 += ord(obj[i + 1])
        total1 += ord(obj[i]) * ord(obj[(i + 1) * -1])

    for i in range(len(obj)):
        if i % 2 == 0:
            total2 += ord(obj[i]) * (i + 1)
        else:
            total2 -= ord(obj[i]) * (i + 1)

    hash = (total1 * total2) % 123456791

    return hash

