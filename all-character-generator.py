exclude = ["\x00", "\x01", "\xf8"]
temp = 'all_chars = (\n"'
for i in range(0, 256):
    if i % 16 == 0 and i != 0:
        temp += '"' + '\n"'
    if not chr(i) in exclude:
        temp += '\\x' + "%0.2X" % i
temp += '"\n)'
print temp
