temp = 'all_chars = ("'
for i in range(0, 256):
    if i % 16 == 0 and i != 0:
        temp += '"' + '\n"'
    temp += '\\x' + "%0.2X" % i
temp += '")'
print temp
