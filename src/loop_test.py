item_list = [3, "string1", 23, 14.0, "string2", 49, 64, 70]

print [i for i in item_list if isinstance(i, int) and i%7 == 0]

