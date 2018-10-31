bindshell = 'bindshell = "'
with open("w32-bind-ngs-shellcode.bin", "rb") as f:
    byte = f.read(1)
    while byte != "":
        byte = f.read(1)
        if len(byte) > 0:
            bindshell += '\\x' + '%02.X' % ord(byte)
bindshell += '"'
print bindshell
        
