import sys

def extractbytes(sh):
    if "\\x" in sh:
        l = sh.split("\\x")
    else:
        l = [sh[i:i+2] for i in range(0, len(sh), 2)]
    return l

def output(sh, typ):
    temp = ""
    l = extractbytes(sh)
    for i in l:
        if len(i) == 2:
            if typ == "bin":
                temp += str(i)
            else:
                temp += "\\x%0.2X" % int(i, 16)
    print temp

def group(sh, numbytes):
    temp = ""
    l = extractbytes(sh)
    counter = 0
    for i in l:
        if len(i) == 2:
            temp += "\\x%0.2X" % int(i, 16)
            counter += 1
            if counter % numbytes == 0:
                temp += "\n"
    if temp.endswith("\n"):
        temp = temp[:-1]
    print temp

def reverse(sh):
    temp = ""
    l = extractbytes(sh)
    l = l[::-1]
    for i in l:
        if len(i) == 2:
            temp += "\\x%0.2X" % int(i, 16)
    return temp

if len(sys.argv) == 2:
    shellcode = sys.argv[1]
    print ""
    print "Original shellcode:"
    output(shellcode, "")
    print ""
    print "Grouped by 4 bytes:"
    group(shellcode, 4)
    print ""
    print "For binary paste:"
    output(shellcode, "bin")
    print ""
    print "Reversed:"
    output(reverse(shellcode), "")
    print ""
    print "Grouped by 4 bytes:"
    group(reverse(shellcode), 4)
    
else:
    print "Usage: python sh-utils.py <shellcode>"
